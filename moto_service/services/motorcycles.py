from typing import Any, Coroutine
from moto_service.repositories.moto_repository import MotorcycleRepository
from moto_service.schemas.motorcycle import Motorcycle, CreateMotorcycleRequest


class MotorcycleService:
    def __init__(self, repository: MotorcycleRepository) -> None:
        self.repository = repository

    def get_all(self) -> Coroutine[Any, Any, list[Motorcycle]]:
        result = self.repository.get_all()
        return result

    def create(self, pet: CreateMotorcycleRequest) -> Coroutine[Any, Any, dict[str, Any]]:
        result = self.repository.create(pet)
        return result

    def get_by_id(self, pet_id: int) -> Coroutine[Any, Any, Motorcycle]:
        result = self.repository.get_by_id(pet_id)
        return result

    def update(self, pet_id: int, item: Motorcycle) -> Coroutine[Any, Any, int]:
        result = self.repository.update(pet_id, item)
        return result

    def delete(self, pet_id: int) -> Coroutine[Any, Any, int]:
        result = self.repository.delete(pet_id)
        return result

    def get_by_client_id(self, client_id):
        result = self.repository.get_by_client_id(client_id)
        return result
