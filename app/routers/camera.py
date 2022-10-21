from fastapi import APIRouter
from fastapi import Response
from pydantic import BaseModel

from app.routers import Health

router = APIRouter(prefix='/camera')


class Image(BaseModel):
    data: bytes


@router.get('/', response_model=Health)
async def health():
    return Health(status='ok')


@router.get('/image/capture', response_model=Image)
# implements http rest api call to capture rpi image
async def capture():
    return Image(data=b'asd')


@router.get('/image/preview')
async def preview():
    return Response(content=b'asd', media_type='image/png')
