from typing import Any
from fastapi import HTTPException

from moto_service.logger import logger
from moto_service.repositories.irepository import IRepository
from moto_service.schemas.motorcycle import Motorcycle, CreateMotorcycleRequest
from moto_service.services.db import motorcycle, database


class MotorcycleRepository(IRepository):
    async def get_all(self) -> list[Motorcycle]:
        query = motorcycle.select()
        pets_list = await database.fetch_all(query)
        if not pets_list:
            msg = "Table 'consultations' is empty"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return pets_list

    async def get_by_id(self, motorcycle_id: int) -> Motorcycle:
        query = motorcycle.select().where(motorcycle.c.motorcycle_id == motorcycle_id)
        pet = await database.fetch_one(query)
        if not pet:
            msg = "Pet didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return pet

    @staticmethod
    async def get_by_client_id(client_id: int) -> list[Motorcycle]:
        query = motorcycle.select().where(motorcycle.c.client_id == client_id)
        pets_list = await database.fetch_all(query)
        if not pets_list:
            msg = "Pets didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return pets_list

    async def create(self, pet: CreateMotorcycleRequest) -> dict[str, Any]:
        query = motorcycle.insert().values(
            client_id=pet.client_id,
            name=pet.name,
            birthday=pet.birthday)
        last_id = await database.execute(query)
        return {**pet.model_dump(), "pet_id": last_id}

    async def update(self, motorcycle_id: int, item: Motorcycle):
        query = motorcycle.update().where(motorcycle.c.motorcycle_id == motorcycle_id).values(**item.model_dump())
        result = await database.execute(query)
        if not result:
            msg = "Pet didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return motorcycle_id

    async def delete(self, motorcycle_id: int):
        query = motorcycle.delete().where(motorcycle.c.motorcycle_id == motorcycle_id)
        result = await database.execute(query)
        if not result:
            msg = "Pet didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return motorcycle_id
