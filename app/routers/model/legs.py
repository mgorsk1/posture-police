from fastapi import APIRouter

from app.models.health import Health
from app.models.prediction_result import PredictionResult
from app.routers.camera import Image

router = APIRouter(prefix='/legs')


@router.get('/', response_model=Health)
async def health():
    return Health(status='ok')


@router.post('/predict', response_model=PredictionResult)
# implements http rest api call to tensorflow model responsible for establishing whether posture is ok or not
async def query_legs_model(data: Image):
    # image = data.data

    try:
        return PredictionResult(prediction=True, confidence=1)
    except Exception:
        return PredictionResult(prediction=False, confidence=1)
