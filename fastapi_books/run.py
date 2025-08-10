import uvicorn

def run_dev():
  uvicorn.run("fastapi_books.main:app", port=4000, reload=True)

def run_prod():
  uvicorn.run("fastapi_books.main:app", port=5000)