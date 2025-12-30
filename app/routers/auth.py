from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User
from ..schemas.user import UserCreate, UserLogin, ChangePassword
from ..core.security import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])

# Signup
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # OAuth2PasswordRequestForm uses "username"
    email = form_data.username
    password = form_data.password

    db_user = db.query(User).filter(User.email == email).first()

    if not db_user or not verify_password(password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # JWT token with user_id, email, exp (30 min)
    access_token = create_access_token(
        user_id=db_user.id,
        email=db_user.email
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# Change Password
@router.post("/change-password")
def change_password(payload: ChangePassword, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == payload.email).first()
    if not db_user or not verify_password(payload.old_password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    db_user.password = hash_password(payload.new_password)
    db.commit()
    return {"message": "Password updated successfully"}

