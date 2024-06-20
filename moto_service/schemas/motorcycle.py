from datetime import date
from pydantic import BaseModel


class CreateMotorcycleRequest(BaseModel):
    client_id: int
    name: str
    birthday: date


class Motorcycle(CreateMotorcycleRequest):
    motorcycle_id: int
    vin: str
    name: str

