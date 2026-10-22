class User:

    def __init__(self, username, role="patron"):
        self._username = username
        self._role = role

    @property
    def username(self):
        return self._username

    @property
    def role(self):
        return self._role

    def is_admin(self):
        return self._role == "admin"

    def to_dict(self):
        return {"username": self._username, "role": self._role}

    @classmethod
    def from_dict(cls, data):
        if data["role"] == "admin":
            return Admin(data["username"])
        return User(data["username"])

    def __str__(self):
        return self._username + " (" + self._role + ")"


class Admin(User):

    def __init__(self, username):
        super().__init__(username, role="admin")