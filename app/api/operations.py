from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status
)

from ..models.operations import (
    Operation, 
    OperationKind, 
    OperationCreate, 
    OperationUpdate
)

from ..models.auth import User

from ..services.operations import OperationService
from ..services.auth import get_current_user

router = APIRouter(
    prefix="/operations",
    tags=["operations"]
)


@router.get("/", response_model=List[Operation])
def get_operations(
    kind: Optional[OperationKind] = None,
    service: OperationService = Depends(),
    user: User = Depends(get_current_user)
):
    return service.get_list(
        kind=kind,
        user_id=user.id
    )


@router.post("/", response_model=Operation)
def create_operation(
    operation_data: OperationCreate, 
    service: OperationService = Depends(),
    user: User = Depends(get_current_user)
):
    return service.create(
        operation_data=operation_data,
        user_id=user.id
    )


@router.get("/{operation_id}", response_model=Operation)
def get_operation(
    operation_id: int,
    service: OperationService = Depends(),
    user: User = Depends(get_current_user)
):
    return service.get(
        operation_id=operation_id,
        user_id=user.id
    )


@router.put("/{operation_id}", response_model=Operation)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    service: OperationService = Depends(),
    user: User = Depends(get_current_user)
):
    return service.update(
        operation_data=operation_data, 
        operation_id=operation_id,
        user_id=user
    )

 
@router.delete("/{operation_id}")
def delete_operation(
    operation_id: int,
    service: OperationService = Depends(),
    user: User = Depends(get_current_user)
):
    service.delete(
        operation_id=operation_id,
        user_id=user.id
    )
    return Response(status_code=status.HTTP_204_NO_CONTENT)