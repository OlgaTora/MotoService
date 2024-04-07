from datetime import date
from pydantic import BaseModel


class CreatePetRequest(BaseModel):
    client_id: int
    name: str
    birthday: date


class Pet(CreatePetRequest):
    pet_id: int
