from datetime import date
from pydantic import BaseModel


class CreateConsultationRequest(BaseModel):
    client_id: int
    pet_id: int
    consultation_date: date
    description: str


class Consultation(CreateConsultationRequest):
    consultation_id: int
