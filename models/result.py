from pydantic import BaseModel


class BaseResult(BaseModel):
    test_id: int
    user_id: int


class ResultCreate(BaseResult):
    num_of_questions: int
    num_of_right: int


class ResultUpdate(BaseResult):
    pass


class Result(BaseResult):
    id: int
    result: float

    class Config:
        orm_mode = True
