from moto_service.repositories.clients_repository import ClientRepository
from moto_service.repositories.consult_repository import ConsultRepository
from moto_service.repositories.moto_repository import MotorcycleRepository

from moto_service.services.clients import ClientService
from moto_service.services.consults import ConsultationService
from moto_service.services.motorcycles import MotorcycleService

# repository - работа с БД
client_repository = ClientRepository()
motorcycle_repository = MotorcycleRepository()
consult_repository = ConsultRepository()

# service - слой UseCase
client_service = ClientService(client_repository)
motorcycle_service = MotorcycleService(motorcycle_repository)
consult_service = ConsultationService(consult_repository)


def get_client_service() -> ClientService:
    return client_service


def get_motorcycle_service() -> MotorcycleService:
    return motorcycle_service


def get_consult_service() -> ConsultationService:
    return consult_service
