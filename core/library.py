from models.book import Book
from models.user import User, Admin
from models.transaction import Transaction, new_transaction
from utils.storage import StorageManager

class LibrarySystem:
    def __init__(self):
        self.storage = StorageManager()
        self.books = [Book.from_dict(d) for d in self.storage.load("books")]
        self.users = [User.from_dict(d) for d in self.storage.load("users")]
        self.loans = [Transaction.from_dict(d) for d in self.storage.load("transactions")]

    def save(self):
        self.storage.save("books", [b.to_dict() for b in self.books])
        self.storage.save("users", [u.to_dict() for u in self.users])
        self.storage.save("transactions", [t.to_dict() for t in self.loans])

    def borrow_book(self, user, book_id):
        for book in self.books:
            if book.id == book_id and book.is_available():
                book.available_copies -= 1
                self.loans.append(new_transaction(len(self.loans) + 1, user.username, book_id))
                print("Borrowed! Due back in 14 days.")
                return
        print("That book is not available.")

    def return_book(self, user, book_id):
        for loan in self.loans:
            if loan.username == user.username and loan.book_id == book_id and loan.status == "borrowed":
                loan.mark_returned()
                self.books[book_id - 1].available_copies += 1
                print("Returned. Thank you!")
                return
        print("You haven't borrowed that book.")

    def run(self):
        name = input("Your name (type 'librarian' for staff): ")
        user = User(name)
        if name == "librarian":
            user = Admin(name)
        if name not in [u.username for u in self.users]:
            self.users.append(user)
        while True:
            choice = input("\n1. View books  2. Borrow  3. Return  4. Add book (staff)  5. Exit\nChoose: ")
            if choice == "1":
                for book in self.books:
                    print(book)
            elif choice == "2":
                self.borrow_book(user, int(input("Book ID: ")))
            elif choice == "3":
                self.return_book(user, int(input("Book ID: ")))
            elif choice == "4" and user.is_admin():
                self.books.append(Book(len(self.books) + 1, input("Title: "), input("Author: "), int(input("Copies: "))))
            elif choice == "5":
                print("Goodbye!")
                break
            self.save()