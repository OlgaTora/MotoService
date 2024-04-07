from typing import Any, Coroutine
from Arcitecture.Seminar_10.clinic.repositories.pets_repository import PetRepository
from Arcitecture.Seminar_10.clinic.schemas.pet import Pet, CreatePetRequest


class PetService:
    def __init__(self, repository: PetRepository) -> None:
        self.repository = repository

    def get_all(self) -> Coroutine[Any, Any, list[Pet]]:
        result = self.repository.get_all()
        return result

    def create(self, pet: CreatePetRequest) -> Coroutine[Any, Any, dict[str, Any]]:
        result = self.repository.create(pet)
        return result

    def get_by_id(self, pet_id: int) -> Coroutine[Any, Any, Pet]:
        result = self.repository.get_by_id(pet_id)
        return result

    def update(self, pet_id: int, item: Pet) -> Coroutine[Any, Any, int]:
        result = self.repository.update(pet_id, item)
        return result

    def delete(self, pet_id: int) -> Coroutine[Any, Any, int]:
        result = self.repository.delete(pet_id)
        return result

    def get_by_client_id(self, client_id):
        result = self.repository.get_by_client_id(client_id)
        return result
