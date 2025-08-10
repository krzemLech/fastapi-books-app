from fastapi import APIRouter, Response
from fastapi_books.dto.books import BookOut, Book, BookUpdate

router = APIRouter(tags=['books'])

sample_book = {
  "id": 1,
  "title": "Sample Book",
  "author": "John Doe",
  "isbn": "12345",
  "pages": 30,
  "rating": 4
}

@router.get("/")
def get_books() -> list[BookOut]:
  return [sample_book]

@router.get("/{id}")
def get_one_book(id: int) -> BookOut:
  print(id)
  return sample_book

@router.post("/")
def create_book(book: Book) -> BookOut:
  print(book)
  return sample_book

@router.patch("/{id}")
def update_book(id: int, book: BookUpdate) -> BookOut:
  print(id, book)
  return sample_book

@router.delete("/{id}", status_code=204)
def delete_book(id: int) -> None:
  print(id)
  return Response(status_code=204)

