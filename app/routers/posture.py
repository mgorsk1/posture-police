from fastapi import APIRouter
from fastapi import status

from app.models.posture_check import PostureCheck
from app.routers.camera import capture
from app.routers.model.legs import query_legs_model
from app.utils.constanst import Kinds

router = APIRouter(prefix='/posture')


@router.get('/check/{kind}', response_model=PostureCheck, status_code=status.HTTP_202_ACCEPTED)
# captures photo and sends it to model to get prediction
async def check_posture(kind: Kinds):
    image = await capture()
    if kind == Kinds.LEGS:
        model = query_legs_model
    else:
        raise NotImplementedError('kind: {} is not implemented.')

    prediction = await model(image)

    return PostureCheck(image=image.data, prediction=prediction, kind=kind)
