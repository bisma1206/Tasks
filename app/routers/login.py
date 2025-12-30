# @router.post("/login")
# def login(
#     form_data: OAuth2PasswordRequestForm = Depends(),
#     db: Session = Depends(get_db)
# ):
#     # OAuth2PasswordRequestForm uses "username"
#     email = form_data.username
#     password = form_data.password

#     db_user = db.query(User).filter(User.email == email).first()

#     if not db_user or not verify_password(password, db_user.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     # JWT token with user_id, email, exp (30 min)
#     access_token = create_access_token(
#         user_id=db_user.id,
#         email=db_user.email
#     )

#     return {
#         "access_token": access_token,
#         "token_type": "bearer"
#     }
