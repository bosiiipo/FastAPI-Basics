from fastapi import FastAPI
from core.config import settings

from db.base import Base
from db.session import engine

from apis.app_router import page_router

def include_router(app): 
    app.include_router(page_router)

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(
        # title=settings.PROJECT_NAME,
        # version=settings.PROJECT_VERSION,
        # docs_url="/docs",
        # openapi_url="/openapi.json"
    )
    include_router(app)
    create_tables()
    return app

app = start_application()

# @app.get("/")
# def hello_api():
#     return {"message": "hello api"}

# @app.get("/about")
# def about():
#     return {"message": "This is our about page"}

# @app.get("/contact")
# def contact():
#     return {"message": "This is the contact page"}

# @app.get("/services")
# def services():
#     return {"message": "This is the service page"} 