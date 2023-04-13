from pydantic import BaseModel


class BaseQuestion(BaseModel):
    text: str
    test_id: int


class QuestionCreate(BaseQuestion):
    pass


class QuestionUpdate(BaseQuestion):
    pass


class Question(BaseQuestion):
    id: int

    class Config:
        orm_mode = True
