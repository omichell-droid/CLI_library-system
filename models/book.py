class Book:
    """A book in the library catalog."""

    def __init__(self, id, title, author, total_copies, available_copies=None):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        # A new book starts with all copies available
        if available_copies is None:
            available_copies = total_copies
        self._available_copies = available_copies

    @property
    def available_copies(self):
        return self._available_copies

    @available_copies.setter
    def available_copies(self, value):
        # Copies can never go below 0 or above the total
        if value < 0 or value > self.total_copies:
            raise ValueError("Copies must be between 0 and the total")
        self._available_copies = value

    def is_available(self):
        return self.available_copies > 0

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["author"],
            data["total_copies"],
            data.get("available_copies"),
        )

    def __str__(self):
        status = "Available" if self.is_available() else "Not available"
        return f"[{self.id}] {self.title} by {self.author} - {self.available_copies} copies ({status})"