import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.library import LibrarySystem
from models.book import Book
from models.user import User, Admin
from utils.storage import StorageManager


def make_library(tmp_path):
    library = LibrarySystem(str(tmp_path))
    library.books.append(Book(1, "Test Book", "Me", 2))
    return library


def test_borrow_book(tmp_path):
    library = make_library(tmp_path)
    assert library.borrow_book(User("leslie"), 1) == True
    assert library.find_book(1).available_copies == 1


def test_cannot_borrow_twice(tmp_path):
    library = make_library(tmp_path)
    user = User("leslie")
    library.borrow_book(user, 1)
    assert library.borrow_book(user, 1) == False


def test_cannot_borrow_unknown_book(tmp_path):
    library = make_library(tmp_path)
    assert library.borrow_book(User("leslie"), 99) == False


def test_return_book(tmp_path):
    library = make_library(tmp_path)
    user = User("leslie")
    library.borrow_book(user, 1)
    assert library.return_book(user, 1) == True
    assert library.find_book(1).available_copies == 2


def test_return_without_borrowing(tmp_path):
    library = make_library(tmp_path)
    assert library.return_book(User("leslie"), 1) == False


def test_patron_cannot_add_book(tmp_path):
    library = make_library(tmp_path)
    library.add_book(User("leslie"), "New", "Author", 1)
    assert len(library.books) == 1


def test_librarian_can_add_book(tmp_path):
    library = make_library(tmp_path)
    library.add_book(Admin("librarian"), "New", "Author", 1)
    assert len(library.books) == 2


def test_data_is_saved(tmp_path):
    library = make_library(tmp_path)
    library.borrow_book(User("leslie"), 1)
    library.save()
    new_library = LibrarySystem(str(tmp_path))
    assert len(new_library.loans) == 1


def test_damaged_json_file(tmp_path):
    (tmp_path / "books.json").write_text("this is not json")
    storage = StorageManager(str(tmp_path))
    assert storage.load("books") == []


def test_menu_with_fake_input(tmp_path, monkeypatch):
    library = make_library(tmp_path)
    answers = iter(["leslie", "2", "1", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))
    library.run()
    assert library.find_book(1).available_copies == 1