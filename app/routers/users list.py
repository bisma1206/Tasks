# add users list.py
# @router.get("/admin/users", response_model=list[UserProfile])
# def list_users(db: Session = Depends(get_db)):
#     """
#     Return list of all users (password excluded)
#     """
#     users = db.query(User).all()
#     return users
