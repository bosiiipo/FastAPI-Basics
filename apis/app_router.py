from fastapi import APIRouter

page_router = APIRouter()

@page_router.get("/")
async def home():
    return {"message": "We are in the home page"}

@page_router.get("/about")
async def about():
    return {"message": "We are in the about page"}
