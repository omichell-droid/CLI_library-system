class User:

    def __init__(self, username, role="patron"):
        self.username = username
        self.role = role

    def is_admin(self):
        return self.role == "admin"

    def to_dict(self):
        return {"username": self.username, "role": self.role}

    @classmethod
    def from_dict(cls, data):
        if data["role"] == "admin":
            return Admin(data["username"])
        return User(data["username"])

    def __str__(self):
        return self.username + " (" + self.role + ")"


class Admin(User):

    def __init__(self, username):
        super().__init__(username, role="admin")