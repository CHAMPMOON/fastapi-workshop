from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter
from fastapi import Depends

from ..models.operations import Operation
from .. import tables
from ..database import get_session


router = APIRouter(
    prefix="/operations"
)


@router.get("/", response_model=List[Operation])
def get_operations(session: Session = Depends(get_session)):
    operations = (
        session
        .query(tables.Operation)
        .all()
    )
    return operations