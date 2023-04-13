from typing import List

from fastapi import APIRouter, Depends, status, Response

from models import Question, QuestionUpdate, QuestionCreate
from services.question import QuestionService

router = APIRouter(
    prefix="/questions",
    tags=['questions']
)


@router.get('/{question_id}', response_model=Question)
def get_question(question_id: int, question_service: QuestionService = Depends()):
    return question_service.get_by_id(question_id)


@router.post('/', response_model=Question, status_code=status.HTTP_201_CREATED)
def create_question(question_data: QuestionCreate, question_service: QuestionService = Depends()):
    return question_service.create(question_data)


@router.put('/{question_id}', response_model=Question)
def update_question(question_id: int, question_data: QuestionUpdate, question_service: QuestionService = Depends()):
    return question_service.update(question_id, question_data)


@router.delete('/{question_id}', response_model=Question)
def delete_question(question_id: int, question_service: QuestionService = Depends()):
    question_service.delete(question_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
