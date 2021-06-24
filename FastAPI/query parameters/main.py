from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{
    "item_name": "Foo"
  }, {
    "item_name": "Bar"
  }, {
    "item_name": "Baz"
  }
]

# Query Parameters with default values
@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
  return fake_items_db[skip : limit + skip]

# Optional Query Parameters
from typing import Optional

@app.get('/items/{item_id}')
async def read_item2(item_id: str, q: Optional[str] = None):
  value = {
    "item_id": item_id
  }
  if q:
    value["q"] = q
  return value