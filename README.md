# CLI Library System

A command-line library system written in Python. Members can view, borrow and return books, and the librarian can add new books. All data is saved to JSON files, so nothing is lost when the program closes.

Group 7: Michell Okwaro and Leslie Kibor

## How to run

You need Python 3. From the project folder:

```
python3 main.py
```

To run the tests:

```
python3 tests/test_models.py
```

## Using the program

Enter your name when the program starts. Type `librarian` to log in as staff. New names are added as members automatically.

1. View books
2. Borrow a book (by Book ID)
3. Return a book (by Book ID)
4. Add a book (librarian only)
5. Exit

Books are lent for 14 days.

## Project structure

```
CLI_library-system/
├── main.py              Starts the program
├── core/library.py      LibrarySystem: menu and library logic
├── models/book.py       Book class
├── models/user.py       User and Admin classes
├── models/transaction.py  Transaction class (one loan)
├── utils/storage.py     StorageManager: reads and writes JSON files
├── tests/test_models.py Tests for the models and storage
└── data/                Created automatically, not uploaded to GitHub
```

## Who did what

- **Michell:** project setup, Book and Transaction models, main.py, tests, README
- **Leslie:** StorageManager, User and Admin models, LibrarySystem, code reviews

## Git workflow

Each feature was built on its own branch, opened as a pull request, reviewed by the other person, and merged into `main`.