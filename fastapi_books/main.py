from fastapi import FastAPI
from fastapi_books.routes.books import router as book_router
from fastapi_books.routes.ratings import router as rating_router

app = FastAPI()

@app.get("/")
def index():
  return { 'status': 'ok' }

app.include_router(book_router, prefix="/api/v1/books")
app.include_router(rating_router, prefix="/api/v1/ratings")