from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


books = [
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "year": 1937,
    },
    {
        "id": 2,
        "title": "A Wrinkle in Time",
        "author": "Madeleine L'Engle",
        "year": 1962,
    },
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Catalog API"}


@app.get("/books")
def list_books():
    # TODO: Return the complete catalog.
    return []


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    # TODO: Generate an ID, save the new book, and return it.
    return book


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find the book by ID or raise HTTPException with status 404.
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove the book by ID and return a confirmation message.
    raise HTTPException(status_code=404, detail="Book not found")
