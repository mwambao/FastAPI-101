'''
Install fastAPI:
***************
#pip install fastAPI

#pip install uvicorn 
uvicorn is the server you will be using to run your API.

To run the below we run:
#uvicorn main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

main --> is main.py file we are running
--reload --> helps not need to stop uvicorn incase we make changes to our project. we just need to refresh the browser.

/hello --> is the endpoint
Therefore we will use on browser: http://127.0.0.1:8000/hello

API Methods:

GET - Read Data
POST - Create Data
PUT - Update Data
DELETE - Delete Data

'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return "Welcome to my fastAPI tutorial"


