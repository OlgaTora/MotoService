from typing import Any, Dict
from fastapi import HTTPException

from Arcitecture.Seminar_10.clinic.logger import logger
from Arcitecture.Seminar_10.clinic.repositories.irepository import IRepository
from Arcitecture.Seminar_10.clinic.schemas.client import Client, CreateClientRequest
from Arcitecture.Seminar_10.clinic.services.db import clients, database


class ClientRepository(IRepository):

    async def get_all(self) -> list[Client]:
        query = clients.select()
        clients_list = await database.fetch_all(query)
        if not clients_list:
            msg = "Table 'clients' is empty"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return clients_list

    async def get_by_id(self, client_id: int) -> Client:
        query = clients.select().where(clients.c.client_id == client_id)
        client = await database.fetch_one(query)
        if not client:
            msg = "User didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return client

    async def create(self, client: CreateClientRequest) -> dict[str, Any]:
        query = clients.insert().values(
            document=client.document,
            surname=client.surname,
            firstname=client.firstname,
            patronymic=client.patronymic,
            birthday=client.birthday)
        last_id = await database.execute(query)
        return {**client.model_dump(), "client_id": last_id}

    async def update(self, client_id: int, item: Client) -> int:
        query = clients.update().where(clients.c.client_id == client_id).values(**item.model_dump())
        result = await database.execute(query)
        if not result:
            msg = "User didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return client_id

    async def delete(self, client_id: int) -> int:
        query = clients.delete().where(clients.c.client_id == client_id)
        result = await database.execute(query)
        if not result:
            msg = "User didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return client_id
