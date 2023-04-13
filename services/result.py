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

from models import ResultCreate, ResultUpdate
from database import Result

from database import get_session


class ResultService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_by_id(self, test_id: int) -> Result:
        result = self._get(test_id)
        return result

    def get_by_user(self, user_id: int) -> List[Result]:
        results = (
            self.session
            .query(Result)
            .filter(Result.user_id == user_id)
            .all()
        )
        return results

    def get_by_test(self, test_id: int) -> List[Result]:
        results = (
            self.session
            .query(Result)
            .filter(Result.test_id == test_id)
            .all()
        )
        return results

    def create(self, test_data: ResultCreate) -> Result:
        raw_result_data = test_data.dict()
        raw_result = raw_result_data['num_of_right'] / raw_result_data['num_of_questions']
        del raw_result_data['num_of_right']
        del raw_result_data['num_of_questions']
        raw_result_data['result'] = raw_result
        result = Result(
            **raw_result_data
        )
        self.session.add(result)
        self.session.commit()
        return result

    def update(self, test_id: int, test_data: ResultUpdate) -> Result:
        result = self._get(test_id)
        for field, value in test_data:
            setattr(result, field, value)
        self.session.commit()
        return result

    def delete(self, test_id: int):
        test = self._get(test_id)
        self.session.delete(test)
        self.session.commit()

    def _get(self, test_id: int) -> Optional[Result]:
        result = (
            self.session
            .query(Result)
            .filter(
                Result.id == test_id,
            )
            .first()
        )
        if not result:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return result
