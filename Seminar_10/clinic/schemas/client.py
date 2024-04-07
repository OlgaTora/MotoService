from datetime import date
from pydantic import BaseModel


class CreateClientRequest(BaseModel):
    document: str
    surname: str
    firstname: str
    patronymic: str
    birthday: date


class Client(CreateClientRequest):
    client_id: int

