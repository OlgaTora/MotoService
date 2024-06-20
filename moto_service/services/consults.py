from typing import Any, Coroutine
from moto_service.repositories.consult_repository import ConsultRepository
from moto_service.schemas.consultation import Consultation, CreateConsultationRequest


class ConsultationService:
    def __init__(self, repository: ConsultRepository) -> None:
        self.repository = repository

    def get_all(self) -> Coroutine[Any, Any, list[Consultation]]:
        result = self.repository.get_all()
        return result

    def create(self, consultation: CreateConsultationRequest) -> Coroutine[Any, Any, dict[str, Any]]:
        result = self.repository.create(consultation)
        return result

    def get_by_id(self, consultation_id: int) -> Coroutine[Any, Any, Consultation]:
        result = self.repository.get_by_id(consultation_id)
        return result

    def update(self, consultation_id: int, item: Consultation) -> Coroutine[Any, Any, int]:
        result = self.repository.update(consultation_id, item)
        return result

    def delete(self, consultation_id: int) -> Coroutine[Any, Any, int]:
        result = self.repository.delete(consultation_id)
        return result

    def get_by_date(self, consultation_date):
        result = self.repository.get_by_date(consultation_date)
        return result
