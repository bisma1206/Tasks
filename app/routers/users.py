from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User
from ..schemas.user import UserProfile, UserUpdate
from fastapi.security import OAuth2PasswordBearer
from ..core.security import verify_token

router = APIRouter(tags=["Users"])

# Use OAuth2PasswordBearer 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Dependency to get current user
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    user_id = payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

# Get profile
@router.get("/profile", response_model=UserProfile)
def get_profile(current_user: User = Depends(get_current_user)):
    """
    Return the authenticated user's profile
    """
    return current_user

# Update profile
@router.put("/profile/update", response_model=UserProfile)
def update_profile(update: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Update the authenticated user's firstname and/or lastname
    """
    if not update.firstname and not update.lastname:
        raise HTTPException(status_code=400, detail="At least one field must be provided")
    
    if update.firstname:
        current_user.firstname = update.firstname
    if update.lastname:
        current_user.lastname = update.lastname
    
    db.commit()
    db.refresh(current_user)
    return current_user

# List all users
@router.get("/admin/users", response_model=list[UserProfile])
def list_users(db: Session = Depends(get_db)):
    """
    Return list of all users (password excluded)
    """
    users = db.query(User).all()
    return users
