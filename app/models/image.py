from pydantic import BaseModel


class Image(BaseModel):
    data: bytes
