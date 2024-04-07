from typing import List, Any
from fastapi import APIRouter, Depends
from Seminar_10.clinic.schemas.client import Client
from Seminar_10.clinic.schemas.client import CreateClientRequest
from Seminar_10.clinic.services.clients import ClientService
from Seminar_10.clinic.services.depends import get_client_service

router = APIRouter()


@router.get('/get-all-clients/',
            responses={400: {'description': 'Bad request'}},
            response_model=List[Client],
            description='Get all clients', )
async def get_all_clients(client_service: ClientService = Depends(get_client_service)) -> List[Client]:
    clients = await client_service.get_all()
    return clients


@router.post('/create-new-client/',
             responses={400: {'description': 'Bad request'}},
             response_model=Client,
             description='Create client', )
async def create_client(new_client: CreateClientRequest, client_service: ClientService = Depends(get_client_service)) -> \
        dict[str, Any]:
    result = await client_service.create(new_client)
    return result


@router.get('/get-client-by-id/{client_id}', responses={400: {'description': 'Bad request'}},
            response_model=Client,
            description='Search client by id')
async def get_client_by_id(client_id: int, client_service: ClientService = Depends(get_client_service)) -> Client:
    result = await client_service.get_by_id(client_id)
    return result


@router.delete('/delete-client/{client_id}', responses={400: {'description': 'Bad request'}},
               response_model=int,
               description='Delete client by id')
async def delete_client(client_id: int, client_service: ClientService = Depends(get_client_service)) -> int:
    result = await client_service.delete(client_id)
    return result


@router.put('/update-client/{client_id}', responses={400: {'description': 'Bad request'}},
            response_model=int,
            description='Update client by id')
async def update_client(client_id: int, item: Client,
                        client_service: ClientService = Depends(get_client_service)) -> int:
    result = await client_service.update(client_id, item)
    return result
