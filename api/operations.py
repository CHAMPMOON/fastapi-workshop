from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends

from ..models.operations import (
    Operation, 
    OperationKind, 
    OperationCreate, 
    OperationUpdate
)
from ..services.operations import OperationService


router = APIRouter(
    prefix="/operations"
)


@router.get("/", response_model=List[Operation])
def get_operations(
    kind: Optional[OperationKind] = None,
    service: OperationService = Depends()
):
    return service.get_list(kind=kind)


@router.post("/", response_model=Operation)
def create_operation(
    operation_date: OperationCreate, 
    service: OperationService = Depends()
):
    return service.create(operation_date)


@router.get("/{operation_id}", response_model=Operation)
def get_operation(
    operation_id: int,
    service: OperationService = Depends()
):
    return service.get(operation_id)


@router.put("/{operation_id}", response_model=Operation)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    service: OperationService = Depends()
):
    return service.update(
        operation_data, 
        operation_id
    )
