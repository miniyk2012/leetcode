# Free yourself from your ORM with mypy!
# https://www.youtube.com/watch?v=oLvEXiV0L-Q&t=476s
from typing import Optional, Dict, cast

from mypy_extensions import TypedDict


class DB:
    def find(self, request: dict) -> Optional[Dict]:
        return {}

    def insert(self, request: dict) -> None:
        return None


db = DB()


def greeting(name: str) -> str:
    return "hello" + name


class Book(TypedDict):
    author: str
    title: str
    publisher: str


class BookSeries(Book):
    series: str


def parse_book(request: dict) -> Book:
    return Book(author=request["author"], title=request["title"], publisher=request["publisher"])


def parse_book_series(request: dict) -> BookSeries:
    return BookSeries(author=request["author"],
                      title=request["title"],
                      publisher=request["publisher"],
                      series=request["series"]
                      )


def save_book(book: Book) -> None:
    db.insert({
        "author": book["author"],
        "title": book["title"],
        "publisher": book["publisher"],
    })


def save_book_in_series(book: BookSeries) -> None:
    db.insert({
        "author": book["author"],
        "title": book["title"],
        "publisher": book["publisher"],
        "series": book["series"],
    })


def find_related(book: Book) -> Optional[Book]:
    if "series" in book:
        return find_in_series(cast(BookSeries, book))
    return None


def find_in_series(book: BookSeries) -> Optional[BookSeries]:
    row = db.find({"series": book["series"]})
    if row is not None:
        return parse_book_series(row)
    else:
        return None


def main():
    book = parse_book_series({'series': 'niubi', 'author': '杨', 'title': 'best', 'publisher': 'af'})
    print('series' in book)


if __name__ == '__main__':
    main()
