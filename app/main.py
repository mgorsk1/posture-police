import logging

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from app.routers.admin import router as admin_router
from app.routers.camera import router as camera_router
from app.routers.model import router as model_router
from app.routers.posture import check_legs
from app.routers.posture import router as posture_router

app = FastAPI()

app.include_router(camera_router)
app.include_router(model_router)
app.include_router(posture_router)
app.include_router(admin_router)


@app.on_event('startup')
@repeat_every(seconds=5)
async def poke():
    r = await check_legs()
    logging.warning(r.json())
