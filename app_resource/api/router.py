from fastapi import APIRouter

from app_resource.api.v1.endpoints import health

api_router = APIRouter()

api_router.include_router(health.router)
