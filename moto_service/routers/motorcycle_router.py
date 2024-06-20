from typing import List, Any
from fastapi import APIRouter, Depends
from moto_service.schemas.motorcycle import Motorcycle, CreateMotorcycleRequest
from moto_service.services.depends import get_motorcycle_service
from moto_service.services.motorcycles import MotorcycleService

router = APIRouter()


@router.get('/get-all-pets/',
            responses={400: {'description': 'Bad request'}},
            response_model=List[Motorcycle],
            description='Get all pets', )
async def get_all_pets(pet_service: MotorcycleService = Depends(get_motorcycle_service)) -> List[Motorcycle]:
    pets = await pet_service.get_all()
    return pets


@router.post('/create-new-pet/',
             responses={400: {'description': 'Bad request'}},
             response_model=Motorcycle,
             description='Create client', )
async def create_pet(new_pet: CreateMotorcycleRequest, pet_service: MotorcycleService = Depends(get_motorcycle_service)) -> dict[str, Any]:
    result = await pet_service.create(new_pet)
    return result


@router.get('/get-pet-by-id/{pet_id}', responses={400: {'description': 'Bad request'}},
            response_model=Motorcycle,
            description='Search pet by id')
async def get_pet_by_id(pet_id: int, pet_service: MotorcycleService = Depends(get_motorcycle_service)) -> Motorcycle:
    result = await pet_service.get_by_id(pet_id)
    return result


@router.get('/get-pet-by-client-id/{client_id}', responses={400: {'description': 'Bad request'}},
            response_model=list[Motorcycle],
            description='Search pet by client id')
async def get_pet_by_id(client_id: int, pet_service: MotorcycleService = Depends(get_motorcycle_service)) -> list[Motorcycle]:
    result = await pet_service.get_by_client_id(client_id)
    return result


@router.delete('/delete-pet/{pet_id}', responses={400: {'description': 'Bad request'}},
               response_model=int,
               description='Delete pet by id')
async def delete_pet(pet_id: int, pet_service: MotorcycleService = Depends(get_motorcycle_service)) -> int:
    result = await pet_service.delete(pet_id)
    return result


@router.put('/update-pet/{pet_id}', responses={400: {'description': 'Bad request'}},
            response_model=int,
            description='Update pet by id')
async def update_pet(pet_id: int, item: Motorcycle, pet_service: MotorcycleService = Depends(get_motorcycle_service)) -> int:
    result = await pet_service.update(pet_id, item)
    return result
