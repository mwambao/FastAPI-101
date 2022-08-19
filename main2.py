
'''
- We can also pass additional parameters on the endpoint.
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def hello(name):
    return f"Welcome to my fastAPI tutorial {name}"