from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app_resource.database.database import get_db_sessionMB


DBSessionMB = Annotated[
    Session,
    Depends(get_db_sessionMB)
]
