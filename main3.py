
'''
- Since we don't have a database, lets try to use a local database
- If i run below on browser:
http://127.0.0.1:8000/get_items/swahili
Output:
["Samosa","Chapati"]

http://127.0.0.1:8000/get_items/american
Output:
["Hot Dog","Apple Pie"]

http://127.0.0.1:8000/get_items/italian
Output:
["Ravioli","Pizza"]

http://127.0.0.1:8000/get_items/mexican
Output:
null

Benefits of fastAPI over Flask:
*******************************
1. fastAPI has IN BUILT DATA VALIDATION, flask doesn't. This make it easier for developers. like we have used below when we create AvailableCuisinces class
If we now supply mexican cuisine, we will get:
"{"detail":[{"loc":["path","cuisine"],"msg":"value is not a valid enumeration member; permitted: 'swahili', 'american', 'italian'","type":"type_error.enum","ctx":{"enum_values":["swahili","american","italian"]}}]}
"
Since fastAPI has this internal validation, this helps to reduce even bugs since you dont have to do validation yourself in code.

In similar manner for the second endpoint:
http://127.0.0.1:8000/get_coupon/2
Output:
{"discount_amount":"20%"}

http://127.0.0.1:8000/get_coupon/rt
Output:
{"detail":[{"loc":["path","code"],"msg":"value is not a valid integer","type":"type_error.integer"}]}

2. fastAPI has IN BUILT DOCUMENTATION
http://127.0.0.1:8000/docs

This generates a swagger UI/documentation for your API.

This is helpful for frontend engineer who will be using your API and can know what you are expecting in backend.
You also can click on 'Try out' and test the API. You will also see a sample curl command used and responses.

Also there is a schema/data section.

http://127.0.0.1:8000/redoc --> Also this provides API documentation

3. Fast running performance. Just as its name, it is very fast. The performance of the server will be as fast just like nodeJS server.

4. Less time to write code, few bugs. Compact code therefore code development will be very fast with few bugs


'''

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableCuisines(str, Enum):
    swahili = "swahili"
    american = "american"
    italian = "italian"

food_items = {
    'swahili' : ["Samosa", "Chapati"],
    'american' : ["Hot Dog", "Apple Pie"],
    'italian' : ["Ravioli", "Pizza"]
}


@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines): #so we are validating if values entered on endpoint are for the cuisines. if not fastapi will capture the error.
    return food_items.get(cuisine)


coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {'discount_amount': coupon_code.get(code)}