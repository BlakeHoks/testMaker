from typing import List

from fastapi import APIRouter, Depends, status, Response

from models import Result, ResultUpdate, ResultCreate
from services.result import ResultService

router = APIRouter(
    prefix="/results",
    tags=['results']
)


@router.get('/user/{user_id}', response_model=List[Result])
def get_results_by_user(user_id: int, result_service: ResultService = Depends()):
    return result_service.get_by_user(user_id)


@router.get('/test/{test_id}', response_model=List[Result])
def get_results_by_test(test_id: int, result_service: ResultService = Depends()):
    return result_service.get_by_test(test_id)


@router.get('/{result_id}', response_model=Result)
def get_results_by_id(result_id: int, result_service: ResultService = Depends()):
    return result_service.get_by_id(result_id)


@router.post('/', response_model=Result, status_code=status.HTTP_201_CREATED)
def create_result(result_data: ResultCreate, result_service: ResultService = Depends()):
    return result_service.create(result_data)


'''
@router.put('/{result_id}', response_model=Result)
def update_result(result_id: int, result_data: ResultUpdate, result_service: ResultService = Depends()):
    return result_service.update(result_id, result_data)
'''


@router.delete('/{result_id}', response_model=Result)
def delete_result(result_id: int, result_service: ResultService = Depends()):
    result_service.delete(result_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
