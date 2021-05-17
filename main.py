from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# initialize app
app = FastAPI()

# pizzas database
db = [
    {
        'id': 0,
        'name': 'Neapolitan Pizza',
        'toppings': ['Basil', 'Onions'],
    },
    {
        'id': 1,
        'name': 'Chicago Pizza',
        'toppings': ['Cheese', 'Tomatoes', 'Onions'],
    },
]

# pizza model
class Pizza(BaseModel):
    name: str
    toppings: List[str]

@app.get('/')
async def index():
    return {"greeting": "Hello, world!"}

# get all pizzas
@app.get('/pizzas')
async def pizzas():
    return db

# get pizza by id
@app.get('/pizzas/{pizza_id}')
async def get_pizzas(pizza_id):
    for pizza in db:
        if(pizza['id'] == int(pizza_id)):
            return pizza
    return {"error": "Pizza not found with id: " + pizza_id }

# create a new pizza
@app.post('/pizzas/create')
async def create_pizza(pizza: Pizza):
    # convert to dictionary
    new_pizza = pizza.dict()
    # add new id
    new_pizza['id'] = db[-1]['id'] + 1
    # add to list
    print(new_pizza)
    db.append(new_pizza)
    return new_pizza