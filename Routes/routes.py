# import modules/packages
from typing import Union
from fastapi import APIRouter

# router instance
router = APIRouter()

# endpoints
@router.get("/test")
async def test():
    return "Test route working"

@router.get("/")
async def home():
    return "Welcome, Dev"

@router.get("/user/{user_name}")
async def user(user_name: str ):
    return "Welcome Dev: {}".format(user_name)

# the q is the query parameter
@router.get("/item/{itemID}")
async def user(itemID: int, q: Union[str, None] = None ):
    return "Item found: {}".format(itemID)