from fastapi import APIRouter, Response
from fastapi_books.dto.ratings import Rating, RatingOut, RatingUpdate

router = APIRouter(tags=['ratings'])

sample_rating = {
  "id": 1,
  "value": 4,
  "author_id": 7,
  "book_id": 2,
}

@router.get("/")
def get_ratings() -> list[RatingOut]:
  return [sample_rating]

@router.get("/{id}")
def get_one_rating(id: int) -> RatingOut:
  print(id)
  return sample_rating

@router.post("/")
def create_rating(rating: Rating) -> RatingOut:
  print(rating)
  return sample_rating

@router.patch("/{id}")
def update_rating(id: int, rating: RatingUpdate) -> RatingOut:
  print(id, rating)
  return sample_rating

@router.delete("/{id}", status_code=204)
def delete_rating(id: int) -> None:
  print(id)
  return Response(status_code=204)