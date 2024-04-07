from typing import Any, Coroutine
from Seminar_10.clinic.repositories.clients_repository import ClientRepository
from Seminar_10.clinic.schemas.client import Client, CreateClientRequest


class ClientService:
    def __init__(self, repository: ClientRepository) -> None:
        self.repository = repository

    def get_all(self) -> Coroutine[Any, Any, list[Client]]:
        result = self.repository.get_all()
        return result

    def create(self, client: CreateClientRequest) -> Coroutine[Any, Any, dict[str, Any]]:
        result = self.repository.create(client)
        return result

    def get_by_id(self, client_id: int) -> Coroutine[Any, Any, Client]:
        result = self.repository.get_by_id(client_id)
        return result

    def update(self, client_id: int, item: Client) -> Coroutine[Any, Any, int]:
        result = self.repository.update(client_id, item)
        return result

    def delete(self, client_id: int) -> Coroutine[Any, Any, int]:
        result = self.repository.delete(client_id)
        return result

