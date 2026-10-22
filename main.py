import argparse

from core.library import LibrarySystem


def main(argv=None):
    parser = argparse.ArgumentParser(description="CLI Library System")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("list", help="Show all books")
    commands.add_parser("menu", help="Start the interactive menu")

    borrow = commands.add_parser("borrow", help="Borrow a book")
    borrow.add_argument("user", help="Your name")
    borrow.add_argument("book_id", type=int, help="ID of the book")

    ret = commands.add_parser("return", help="Return a book")
    ret.add_argument("user", help="Your name")
    ret.add_argument("book_id", type=int, help="ID of the book")

    add = commands.add_parser("add-book", help="Add a book (librarian only)")
    add.add_argument("user", help="Your name")
    add.add_argument("title")
    add.add_argument("author")
    add.add_argument("copies", type=int)

    args = parser.parse_args(argv)
    library = LibrarySystem()

    if args.command == "list":
        library.show_books()
    elif args.command == "menu":
        library.run()
    elif args.command == "borrow":
        library.borrow_book(library.get_user(args.user), args.book_id)
    elif args.command == "return":
        library.return_book(library.get_user(args.user), args.book_id)
    elif args.command == "add-book":
        library.add_book(library.get_user(args.user), args.title, args.author, args.copies)

    library.save()


if __name__ == "__main__":
    main()