from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, users

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Authentication API")

# Routers
app.include_router(auth.router)
app.include_router(users.router)
