from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from Arcitecture.Seminar_10.clinic.schemas.pet import Pet
from Arcitecture.Seminar_10.clinic.schemas.pet import CreatePetRequest
from Arcitecture.Seminar_10.clinic.services.depends import get_pet_service
from Arcitecture.Seminar_10.clinic.services.pets import PetService

router = APIRouter()


@router.get('/get-all-pets/',
            responses={400: {'description': 'Bad request'}},
            response_model=List[Pet],
            description='Get all pets', )
async def get_all_pets(pet_service: PetService = Depends(get_pet_service)) -> List[Pet]:
    pets = await pet_service.get_all()
    return pets


@router.post('/create-new-pet/',
             responses={400: {'description': 'Bad request'}},
             response_model=Pet,
             description='Create client', )
async def create_pet(new_pet: CreatePetRequest, pet_service: PetService = Depends(get_pet_service)) -> dict[str, Any]:
    result = await pet_service.create(new_pet)
    return result


@router.get('/get-pet-by-id/{pet_id}', responses={400: {'description': 'Bad request'}},
            response_model=Pet,
            description='Search pet by id')
async def get_pet_by_id(pet_id: int, pet_service: PetService = Depends(get_pet_service)) -> Pet:
    result = await pet_service.get_by_id(pet_id)
    return result


@router.get('/get-pet-by-client-id/{client_id}', responses={400: {'description': 'Bad request'}},
            response_model=list[Pet],
            description='Search pet by client id')
async def get_pet_by_id(client_id: int, pet_service: PetService = Depends(get_pet_service)) -> list[Pet]:
    result = await pet_service.get_by_client_id(client_id)
    return result


@router.delete('/delete-pet/{pet_id}', responses={400: {'description': 'Bad request'}},
               response_model=int,
               description='Delete pet by id')
async def delete_pet(pet_id: int, pet_service: PetService = Depends(get_pet_service)) -> int:
    result = await pet_service.delete(pet_id)
    return result


@router.put('/update-pet/{pet_id}', responses={400: {'description': 'Bad request'}},
            response_model=int,
            description='Update pet by id')
async def update_pet(pet_id: int, item: Pet, pet_service: PetService = Depends(get_pet_service)) -> int:
    result = await pet_service.update(pet_id, item)
    return result
