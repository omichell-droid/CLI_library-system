import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import main
from core.library import LibrarySystem


def test_list_command(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    main(["list"])


def test_add_book_command(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    main(["add-book", "librarian", "Dune", "Herbert", "2"])
    assert len(LibrarySystem().books) == 1