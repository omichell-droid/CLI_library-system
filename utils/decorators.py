def admin_only(func):
    """Only the librarian can run the function."""
    def wrapper(self, user, *args):
        if not user.is_admin():
            print("Only the librarian can do that.")
            return None
        return func(self, user, *args)
    return wrapper

#stops the user from running the function if they are not the librarian