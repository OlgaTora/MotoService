from Arcitecture.Seminar_10.clinic.repositories.clients_repository import ClientRepository
from Arcitecture.Seminar_10.clinic.repositories.pets_repository import PetRepository
from Arcitecture.Seminar_10.clinic.repositories.consult_repository import ConsultRepository

from Arcitecture.Seminar_10.clinic.services.clients import ClientService
from Arcitecture.Seminar_10.clinic.services.consults import ConsultationService
from Arcitecture.Seminar_10.clinic.services.pets import PetService

# repository - работа с БД
client_repository = ClientRepository()
pet_repository = PetRepository()
consult_repository = ConsultRepository()

# service - слой UseCase
client_service = ClientService(client_repository)
pet_service = PetService(pet_repository)
consult_service = ConsultationService(consult_repository)


def get_client_service() -> ClientService:
    return client_service


def get_pet_service() -> PetService:
    return pet_service


def get_consult_service() -> ConsultationService:
    return consult_service
