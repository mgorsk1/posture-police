from fastapi import APIRouter

from app.models.health import Health

router = APIRouter(prefix='/admin')


@router.get('/health', status_code=200)
async def health():
    return Health(status='ok')
