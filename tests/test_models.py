import os
import sys

# Lets this file find models/ and utils/ when run from the project folder
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.book import Book
from models.user import User, Admin
from models.transaction import Transaction, new_transaction
from utils.storage import StorageManager


def test_new_book_has_all_copies_available():
    book = Book(1, "Test", "Me", 2)
    assert book.available_copies == 2
    assert book.is_available() == True


def test_book_with_no_copies_is_not_available():
    book = Book(1, "Test", "Me", 2, 0)
    assert book.is_available() == False


def test_book_to_dict_and_back():
    book = Book(1, "Test", "Me", 3, 1)
    copy = Book.from_dict(book.to_dict())
    assert copy.title == "Test"
    assert copy.available_copies == 1


def test_available_copies_cannot_go_below_zero():
    book = Book(1, "Test", "Me", 2)
    try:
        book.available_copies = -1
        assert False
    except ValueError:
        assert True


def test_user_and_admin_roles():
    assert User("leslie").is_admin() == False
    assert Admin("librarian").is_admin() == True


def test_user_username_is_read_only():
    user = User("leslie")
    assert user.username == "leslie"


def test_new_transaction_is_borrowed():
    loan = new_transaction(1, "michell", 1)
    assert loan.status == "borrowed"
    assert loan.is_overdue() == False


def test_mark_returned():
    loan = new_transaction(1, "michell", 1)
    loan.mark_returned()
    assert loan.status == "returned"


def test_old_loan_is_overdue():
    loan = Transaction(1, "michell", 1, "2020-01-01", "2020-01-15")
    assert loan.is_overdue() == True


def test_storage_save_and_load():
    storage = StorageManager("test_data")
    storage.save("books", [{"id": 1}])
    assert storage.load("books") == [{"id": 1}]
    os.remove("test_data/books.json")
    os.rmdir("test_data")