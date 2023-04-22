from fastapi import FastAPI
from pydantic import BaseModel


class ResponseBaseModel(BaseModel):
    """Формат ответа"""
    message: str = "pong"


app = FastAPI()


@app.get('/ping', response_model=ResponseBaseModel)
def ping() -> dict:
    return {"message": "pong"}
