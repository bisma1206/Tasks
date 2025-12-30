from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
# JWT CONFIG
SECRET_KEY = "super-secret-key"   
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# PASSWORD HASHING
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    return pwd_context.hash(password)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
# JWT TOKEN
def create_access_token(user_id: int, email: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "user_id": user_id,
        "email": email,
        "exp": expire
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
