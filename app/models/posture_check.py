from pydantic import BaseModel

from app.models.prediction_result import PredictionResult


class PostureCheck(BaseModel):
    image: bytes
    prediction: PredictionResult
    kind: str
