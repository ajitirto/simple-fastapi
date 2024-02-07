from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# GET todo
@app.get("/todos")
async def get_todos():
    return {"todos": todos}