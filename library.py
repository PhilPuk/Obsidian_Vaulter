from pathlib import Path
from logger_config import logger
from obsidian_time import Time
from obsidian_config import ObsidianConfig
from template import my_Template

my_Time = Time()
obs_config = ObsidianConfig()

class Library:
    def __init__(self):
        pass

    def loadAllBooks(self):
        pass

class Book:
    def __init__(self, title: str="None", author: str="None", new_book: bool=True):
        self._title = title.replace(" ", "_")
        self._author = author
        self._books_path = obs_config.getVaultPath() / "Books"
        self._unsorted_books_path = self._books_path / "Unsorted"
        self._books_path.mkdir(parents=True, exist_ok=True)
        self._unsorted_books_path.mkdir(parents=True, exist_ok=True)
        self._current_book_path = self._unsorted_books_path / f"{self._title}.md"
        self._book_page_template = my_Template.getBookPageTemplate()
        if new_book:
            self.fillBookPageWithTemplate()
        logger.info(f"Created new book page for obsidian: {self._title}.md")

    def fillBookPageWithTemplate(self):
        with open(self._current_book_path, 'a') as f:
            f.write(self._book_page_template)        

class BookFactory:
    def __init__(self):
        pass

    def newBook(self, title: str):
        return Book(title)
    
def main():
    logger.info("Starting book creation")
    try:
        my_title = str(input("Enter book title: "))
        Book(title=my_title)
    except Exception as e:
        logger.error(f"Could not create new book due to following exception: '{e}'")
    logger.info("Exiting book creation")

if __name__ == "__main__":
    main()