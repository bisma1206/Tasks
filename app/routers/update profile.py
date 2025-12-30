# @router.put("/profile/update", response_model=UserProfile)
# def update_profile(update: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     """
#     Update the authenticated user's firstname and/or lastname
#     """
#     if not update.firstname and not update.lastname:
#         raise HTTPException(status_code=400, detail="At least one field must be provided")
    
#     if update.firstname:
#         current_user.firstname = update.firstname
#     if update.lastname:
#         current_user.lastname = update.lastname
    
#     db.commit()
#     db.refresh(current_user)
#     return current_user
