from fastapi import APIRouter, HTTPException

from app_resource.database.database import test_database_connectionMB


router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():

    try:
        test_database_connectionMB()

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed"
        )
