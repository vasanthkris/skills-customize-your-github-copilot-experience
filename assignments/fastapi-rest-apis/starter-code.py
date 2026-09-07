"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


books = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937),
    Book(id=2, title="Frankenstein", author="Mary Shelley", year=1818),
]


@app.get("/books")
def list_books():
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return a book, or raise a 404 error.
    pass


@app.post("/books", status_code=201)
def create_book(book: Book):
    # TODO: Add the book and return it.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    # TODO: Replace the matching book, or raise a 404 error.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Delete the matching book, or raise a 404 error.
    pass


# Run with: uvicorn starter-code:app --reload
