from pydantic import BaseModel


class BaseTest(BaseModel):
    author_id: int
    title: str
    amount_of_questions: int


class TestCreate(BaseTest):
    pass


class TestUpdate(BaseTest):
    pass


class Test(BaseTest):
    id: int

    class Config:
        orm_mode = True
