from datetime import date, timedelta

LOAN_DAYS = 14  # how long a book can be borrowed


class Transaction:
    """A record of one book being borrowed (and later returned)."""

    def __init__(self, id, username, book_id, borrow_date, due_date,
                 return_date=None, status="borrowed"):
        self.id = id
        self.username = username
        self.book_id = book_id
        self.borrow_date = borrow_date    # "YYYY-MM-DD"
        self.due_date = due_date          # "YYYY-MM-DD"
        self.return_date = return_date    # None until returned
        self.status = status              # "borrowed", "returned" or "overdue"

    def is_overdue(self):
        return self.status == "borrowed" and date.fromisoformat(self.due_date) < date.today()

    def mark_returned(self):
        self.return_date = date.today().isoformat()
        self.status = "returned"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "book_id": self.book_id,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date,
            "return_date": self.return_date,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["username"],
            data["book_id"],
            data["borrow_date"],
            data["due_date"],
            data.get("return_date"),
            data.get("status", "borrowed"),
        )

    def __str__(self):
        return f"#{self.id} {self.username} - book {self.book_id} - due {self.due_date} - {self.status}"


def new_transaction(id, username, book_id):
    """Create a new 'borrowed' transaction starting today."""
    today = date.today()
    due = today + timedelta(days=LOAN_DAYS)
    return Transaction(id, username, book_id, today.isoformat(), due.isoformat())