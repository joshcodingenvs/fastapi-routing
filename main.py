# import required modules/packages
from typing import Union
from fastapi import FastAPI

# import the routes
from Routes.routes import router

# app instance
app = FastAPI()

# configure the to app instance
app.include_router(router)