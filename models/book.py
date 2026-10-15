class Book:
    """A book in the library catalog."""

    def __init__(self, id, title, author, total_copies, available_copies=None):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        # A new book starts with all copies available
        self.available_copies = total_copies if available_copies is None else available_copies

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