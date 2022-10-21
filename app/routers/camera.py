from fastapi import APIRouter
from fastapi import Response

from app.models.health import Health
from app.models.image import Image

router = APIRouter(prefix='/camera')


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
