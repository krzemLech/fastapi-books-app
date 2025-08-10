from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
  title: str
  author: str
  isbn: str
  pages: int
  rating: int

class BookOut(Book):
  id: int

class BookUpdate(BaseModel):
  title: Optional[str] = None
  author: Optional[str] = None
  isbn: Optional[str] = None
  pages: Optional[int] = None
  rating: Optional[int] = None

  # Programatic option:

# OptionalBook = create_model(
#   'OptionalBook',
#   **{name: (Optional[field.type_], None) for name, field in Book.__fields__.items()}
# )