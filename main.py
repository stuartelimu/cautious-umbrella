from fastapi import FastAPI

# initialize app
app = FastAPI()

@app.get('/')
async def index():
    return {"greeting": "Hello, world!"}