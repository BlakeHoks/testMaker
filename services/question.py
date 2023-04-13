from typing import (
    List,
    Optional,
)

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from models import QuestionUpdate, QuestionCreate
from database import Question

from database import get_session


class QuestionService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_by_id(self, question_id: int) -> Question:
        question = self._get(question_id)
        return question

    def get_by_test(self, test_id: int) -> List[Question]:
        questions = (
            self.session
            .query(Question)
            .filter(Question.test_id == test_id)
            .all()
        )
        return questions

    def create(self, question_data: QuestionCreate) -> Question:
        question = Question(
            **question_data.dict()
        )
        self.session.add(question)
        self.session.commit()
        return question

    def update(self, question_id: int, question_data: QuestionUpdate) -> Question:
        question = self._get(question_id)
        for field, value in question_data:
            setattr(question, field, value)
        self.session.commit()
        return question

    def delete(self, question_id: int):
        question = self._get(question_id)
        self.session.delete(question)
        self.session.commit()

    def _get(self, question_id: int) -> Optional[Question]:
        question = (
            self.session
            .query(Question)
            .filter(
                Question.id == question_id,
            )
            .first()
        )
        if not question:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return question
