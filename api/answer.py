from typing import List

from fastapi import APIRouter, Depends, status, Response

from models import Answer, AnswerUpdate, AnswerCreate
from services.answer import AnswerService

router = APIRouter(
    prefix="/answers",
    tags=['answers']
)


@router.get('/{question_id}', response_model=List[Answer])
def get_answer(question_id: int, answer_service: AnswerService = Depends()):
    return answer_service.get_by_question_id(question_id)


@router.post('/', response_model=Answer, status_code=status.HTTP_201_CREATED)
def create_answer(answer_data: AnswerCreate, answer_service: AnswerService = Depends()):
    return answer_service.create(answer_data)


@router.put('/{answer_id}', response_model=Answer)
def update_answer(answer_id: int, answer_data: AnswerUpdate, answer_service: AnswerService = Depends()):
    return answer_service.update(answer_id, answer_data)


@router.delete('/{answer_id}', response_model=Answer)
def delete_answer(answer_id: int, answer_service: AnswerService = Depends()):
    answer_service.delete(answer_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
