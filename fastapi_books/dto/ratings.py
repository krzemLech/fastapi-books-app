from pydantic import BaseModel
from typing import Optional

class Rating(BaseModel):
  value: int
  author_id: int | str
  book_id: int

class RatingOut(Rating):
  id: int

class RatingUpdate(BaseModel):
  value: Optional[int] = None