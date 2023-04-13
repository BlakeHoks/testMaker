from fastapi import APIRouter

from . import (
    test,
    question,
    auth,
    answer,
    result
)

router = APIRouter()
router.include_router(test.router)
router.include_router(question.router)
router.include_router(auth.router)
router.include_router(answer.router)
router.include_router(result.router)
