import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Boolean,
    Float
)

Base = declarative_base()


def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = sa.create_engine(url)
    return engine


engine = get_engine("postgres", "pass", "localhost", "5432", "TestMaker")


Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False,
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'), index=True)
    text = Column(String)
    status = Column(Boolean)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password_hash = Column(String)


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey('tests.id'), index=True)
    text = Column(String)


class Test(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.id'), index=True)
    title = Column(String)
    amount_of_questions = Column(Integer)


class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey('tests.id'), index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    result = Column(Float)

'''
sc = Session()
Base.metadata.create_all(engine)
sc.commit()
sc.close()
'''