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

from models import TestCreate, TestUpdate
from database import Test

from database import get_session


class TestService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_by_id(self, test_id: int) -> Test:
        test = self._get(test_id)
        return test

    def get_by_author(self, author_id: int) -> List[Test]:
        tests = (
            self.session
            .query(Test)
            .filter(Test.author_id == author_id)
            .all()
        )
        return tests

    def create(self, test_data: TestCreate) -> Test:
        test = Test(
            **test_data.dict()
        )
        self.session.add(test)
        self.session.commit()
        return test

    def update(self, test_id: int, test_data: TestUpdate) -> Test:
        test = self._get(test_id)
        for field, value in test_data:
            setattr(test, field, value)
        self.session.commit()
        return test

    def delete(self, test_id: int):
        test = self._get(test_id)
        self.session.delete(test)
        self.session.commit()

    def _get(self, test_id: int) -> Optional[Test]:
        test = (
            self.session
            .query(Test)
            .filter(
                Test.id == test_id,
            )
            .first()
        )
        if not test:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return test
