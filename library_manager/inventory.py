import json
from pathlib import Path
from library_manager.book import Book
import logging

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def _init_(self, filepath="data/books.json"):
        self.filepath = Path(filepath)
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            if not self.filepath.exists():
                self.filepath.parent.mkdir(exist_ok=True)
                self.filepath.write_text("[]")

            with open(self.filepath, "r") as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]

        except Exception as e:
            logging.error(f"Error loading books: {e}")
            self.books = []

    def save_books(self):
        try:
            with open(self.filepath, "w") as f:
                json.dump([book.to_dict() for book in self.books], f, indent=4)
        except Exception as e:
            logging.error(f"Error saving books: {e}")

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        logging.info(f"Book added: {title}")

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        return self.books