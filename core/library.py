from rich.console import Console
from rich.table import Table

from models.book import Book
from models.user import User, Admin
from models.transaction import Transaction, new_transaction
from utils.storage import StorageManager
from utils.decorators import admin_only

console = Console()


class LibrarySystem:
    def __init__(self, data_folder="data"):
        self.storage = StorageManager(data_folder)
        self.books = [Book.from_dict(d) for d in self.storage.load("books")]
        self.users = [User.from_dict(d) for d in self.storage.load("users")]
        self.loans = [Transaction.from_dict(d) for d in self.storage.load("transactions")]

    def save(self):
        self.storage.save("books", [b.to_dict() for b in self.books])
        self.storage.save("users", [u.to_dict() for u in self.users])
        self.storage.save("transactions", [t.to_dict() for t in self.loans])

    def get_user(self, name):
        """Find a user, or make a new one if the name is new."""
        for user in self.users:
            if user.username == name:
                return user
        if name == "librarian":
            user = Admin(name)
        else:
            user = User(name)
        self.users.append(user)
        return user

    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def show_books(self):
        table = Table(title="Library Books")
        table.add_column("ID")
        table.add_column("Title")
        table.add_column("Author")
        table.add_column("Available")
        for book in self.books:
            table.add_row(str(book.id), book.title, book.author,
                          str(book.available_copies) + "/" + str(book.total_copies))
        console.print(table)

    def borrow_book(self, user, book_id):
        book = self.find_book(book_id)
        if book is None:
            print("No book with that ID.")
            return False
        if not book.is_available():
            print("That book is not available.")
            return False
        for loan in self.loans:
            if loan.username == user.username and loan.book_id == book_id and loan.status == "borrowed":
                print("You already borrowed that book.")
                return False
        book.available_copies -= 1
        self.loans.append(new_transaction(len(self.loans) + 1, user.username, book_id))
        print("Borrowed! Due back in 14 days.")
        return True

    def return_book(self, user, book_id):
        for loan in self.loans:
            if loan.username == user.username and loan.book_id == book_id and loan.status == "borrowed":
                loan.mark_returned()
                self.find_book(book_id).available_copies += 1
                print("Returned. Thank you!")
                return True
        print("You haven't borrowed that book.")
        return False

    @admin_only
    def add_book(self, user, title, author, copies):
        if title == "" or copies < 1:
            print("Please give a title and at least 1 copy.")
            return False
        self.books.append(Book(len(self.books) + 1, title, author, copies))
        print("Book added.")
        return True

    def run(self):
        name = input("Your name (type 'librarian' for staff): ").strip()
        if name == "":
            print("Name cannot be empty.")
            return
        user = self.get_user(name)

        while True:
            choice = input("\n1. View books  2. Borrow  3. Return  4. Add book (staff)  5. Exit\nChoose: ")
            try:
                if choice == "1":
                    self.show_books()
                elif choice == "2":
                    self.borrow_book(user, int(input("Book ID: ")))
                elif choice == "3":
                    self.return_book(user, int(input("Book ID: ")))
                elif choice == "4":
                    self.add_book(user, input("Title: "), input("Author: "), int(input("Copies: ")))
                elif choice == "5":
                    print("Goodbye!")
                    self.save()
                    break
                else:
                    print("Please choose 1 to 5.")
            except ValueError:
                print("Please type a number.")
            self.save()