from pydantic import BaseModel


class PredictionResult(BaseModel):
    prediction: bool
    confidence: float
