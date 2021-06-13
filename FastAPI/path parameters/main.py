from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
  alexnet = 'alexnet'
  resnet = 'resnet'
  lenet = 'lenet'

app = FastAPI()

@app.get('/items/{item_id}')
async def read_item(item_id: int):
  return {
    'item_id': item_id
  }

@app.get('/users/me')
async def read_user_me():
  return {
    'user_id': 'ther current user'
  }

@app.get('/users/{user_id}')
async def read_user(user_id: str):
  return {
    'user_id': user_id
  }

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
  return {
    'mmodel_name': model_name
  }

