from typing import List

from fastapi import APIRouter, Depends, status, Response

from models import Test, TestUpdate, TestCreate
from services.test import TestService
from services.question import QuestionService
from services.answer import AnswerService

router = APIRouter(
    prefix="/tests",
    tags=['tests']
)


@router.get('/{test_id}')
def get_test(test_id: int, test_service: TestService = Depends(), question_service: QuestionService = Depends(), answer_service: AnswerService = Depends()):
    test_info = test_service.get_by_id(test_id)
    questions = question_service.get_by_test(test_id)
    ids_of_questions = []
    for question in questions:
        ids_of_questions.append(question.id)
    answers = []
    for i in ids_of_questions:
        answers.append(answer_service.get_by_question_id(i))
    test = dict([('test_info', test_info), ('questions', questions), ('answers', answers)])
    return test


@router.get('/author/{author_id}', response_model=List[Test])
def get_tests_by_author(author_id: int, test_service: TestService = Depends()):
    return test_service.get_by_author(author_id)


@router.post('/', response_model=Test, status_code=status.HTTP_201_CREATED)
def create_test(test_data: TestCreate, test_service: TestService = Depends()):
    return test_service.create(test_data)


@router.put('/{test_id}', response_model=Test)
def update_test(test_id: int, test_data: TestUpdate, test_service: TestService = Depends()):
    return test_service.update(test_id, test_data)


@router.delete('/{test_id}', response_model=Test)
def delete_test(test_id: int, test_service: TestService = Depends()):
    test_service.delete(test_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
