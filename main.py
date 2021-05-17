from fastapi import FastAPI

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