from io import BytesIO

from fastapi import APIRouter
from fastapi import Response

from app.models.health import Health
from app.models.image import Image
from app.utils.camera import camera

router = APIRouter(prefix='/camera')


@router.get('/', response_model=Health)
async def health():
    return Health(status='ok')


@router.get('/image/capture', response_model=Image)
# implements http rest api call to capture rpi image
async def capture():
    return Image(data=_capture())


@router.get('/image/preview')
async def preview():
    return Response(content=_capture(), media_type='image/png')


def _capture():
    my_stream = BytesIO()
    camera.capture(my_stream, 'png')
    my_stream.seek(0)

    return my_stream.read()
