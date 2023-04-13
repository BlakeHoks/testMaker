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

from models import AnswerCreate, AnswerUpdate
from database import Answer

from database import get_session


class AnswerService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_by_question_id(self, question_id: int) -> List[Answer]:
        answers = (
            self.session
            .query(Answer)
            .filter(Answer.question_id == question_id)
            .all()
        )
        return answers

    def create(self, answer_data: AnswerCreate) -> Answer:
        answer = Answer(
            **answer_data.dict()
        )
        self.session.add(answer)
        self.session.commit()
        return answer

    def update(self, answer_id: int, answer_data: AnswerUpdate) -> Answer:
        answer = self._get(answer_id)
        for field, value in answer_data:
            setattr(answer, field, value)
        self.session.commit()
        return answer

    def delete(self, answer_id: int):
        answer = self._get(answer_id)
        self.session.delete(answer)
        self.session.commit()

    def _get(self, answer_id: int) -> Optional[Answer]:
        answer = (
            self.session
            .query(Answer)
            .filter(
                Answer.id == answer_id,
            )
            .first()
        )
        if not answer:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return answer
