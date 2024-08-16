from uuid import uuid4
from typing import List
from enum import Enum
from fastapi import FastAPI
from model import UserType, User

user_types_data = [{"admin":"Admins have level 0 capabality", "fuel_supplier":"Fuel supplier has level 1 capabilty", "user":"User has level 2 capability"}]

class UserType(str, Enum):
    user = "user"
    admin = "admin"
    fuel_supplier = "fuel_supplier"


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        username="samwaku", 
        email="samuelwaku1st@gmail.com", 
        first_name="samuel", 
        password="1234", 
        roles=[UserType.user]
    ),
    User(
        id=uuid4(), 
        username="adiwaku", 
        email="adiwaku1st@gmail.com", 
        first_name="adrian", 
        password="1234", 
        roles=[UserType.admin, UserType.user]
    )
]

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.post("/post")
async def post():
    return {"message": "hello from the post route"}

@app.get("/items/{item_id}")
async def list_item(item_id: int):
    return {"message": item_id}

@app.get("/useritems")
async def read_users(skip: int = 0, limit: int = 10):
    return db[skip : skip + limit]

@app.get("/users/{user_type}")
async def get_user(user_type: UserType):
    if user_type is UserType.admin:
        return{"usertype ": user_type, "message": "You are a system admin"}
    
    if user_type.user.value:
        return{"usertype ": user_type, "message": "You are a normal system user"}

    if user_type.fuel_supplier.value:
        return{"usertype ": user_type, "message": "You are a fuel supplier"}
