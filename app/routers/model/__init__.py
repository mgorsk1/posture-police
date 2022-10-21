from fastapi import APIRouter

from .legs import router as legs_router


router = APIRouter(prefix='/model')

router.include_router(legs_router)
