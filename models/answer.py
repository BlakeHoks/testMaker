from pydantic import BaseModel


class BaseAnswer(BaseModel):
    question_id: int
    text: str
    status: bool


class AnswerCreate(BaseAnswer):
    pass


class AnswerUpdate(BaseAnswer):
    pass


class Answer(BaseAnswer):
    id: int

    class Config:
        orm_mode = True
