from fastapi import FastAPI
from app_resource.core.config import settings
from app_resource.api.router import api_router
from app_resource.core.logging import setup_loggingMB
    
    
setup_loggingMB(settings.DEBUG)

app = FastAPI(
    title=settings.APP_NAME,
    description="Learning Management System API",
    version="1.0.0"
)

app.include_router(
    api_router,
    prefix="/api/v1"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Hii Learn API"
    }
