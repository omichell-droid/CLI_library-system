# CLI Library System

A command-line library system written in Python, where members can borrow and return books and the librarian can add new ones.

## Description

This project is a library system you use from the terminal. Members can look at the books, borrow a book and return it. The librarian can also add new books. All data is saved in JSON files, so nothing is lost when the program closes.

**Features**
- View all books in a table (made with the `rich` package)
- Borrow and return books by book ID (books are lent for 14 days)
- Librarian-only action for adding books (checked with an `admin_only` decorator)
- Commands built with `argparse`, plus an interactive menu
- Data saved to JSON files, with a safe fallback if a file is damaged
- Tests written with `pytest`

## Requirements

- Python 3
- The packages listed in `requirements.txt` (`rich` and `pytest`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/omichell-droid/CLI_library-system.git
cd CLI_library-system
```

2. Install the packages:

```bash
pip install -r requirements.txt
```

## Usage

Show all books:

```bash
python3 main.py list
```

Borrow a book (your name, then the book ID):

```bash
python3 main.py borrow patron1 1
```

Output: `Borrowed! Due back in 14 days.`

Return a book:

```bash
python3 main.py return patron1 1
```

Output: `Returned. Thank you!`

Add a book (librarian only: name, title, author, copies):

```bash
python3 main.py add-book librarian "Dune" "Frank Herbert" 2
```

Start the interactive menu:

```bash
python3 main.py menu
```

See all commands:

```bash
python3 main.py --help
```

Type `librarian` as your name to log in as staff. Any other new name is added as a member automatically. If a member tries to add a book, the program prints `Only the librarian can do that.`

## Project structure

```
CLI_library-system/
├── main.py                 Starts the program (argparse commands)
├── requirements.txt        Packages to install (rich, pytest)
├── core/library.py         LibrarySystem: menu and library logic
├── models/book.py          Book class
├── models/user.py          User and Admin classes
├── models/transaction.py   Transaction class (one loan)
├── utils/storage.py        StorageManager: reads and writes JSON files
├── utils/decorators.py     admin_only decorator
├── data/                   JSON data files (books, users, transactions)
└── tests/                  Tests for models, library logic and commands
```

## Support

If something does not work, open an issue on the
[GitHub repository](https://github.com/omichell-droid/CLI_library-system/issues).

## Roadmap

Ideas for the future:
- Passwords and registration for members
- A command to show overdue books
- Searching books by title or author

## Contributing

We worked using feature branches. Each feature was built on its own branch, opened as a pull request, reviewed by the other person, and merged into `main`.

To run the tests:

```bash
python3 -m pytest
```

## Authors and acknowledgment

Group 7: Michell Okwaro and Leslie Kibor

- **Michell:** project setup, Book and Transaction models, main.py, tests, README
- **Leslie:** StorageManager, User and Admin models, LibrarySystem, code reviews

## Project status

Finished for the course assignment.