from typing import Any
from fastapi import HTTPException

from Seminar_10.clinic.logger import logger
from Seminar_10.clinic.repositories.irepository import IRepository
from Seminar_10.clinic.schemas.pet import Pet, CreatePetRequest
from Seminar_10.clinic.services.db import pets, database


class PetRepository(IRepository):
    async def get_all(self) -> list[Pet]:
        query = pets.select()
        pets_list = await database.fetch_all(query)
        if not pets_list:
            msg = "Table 'consultations' is empty"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return pets_list

    async def get_by_id(self, pet_id: int) -> Pet:
        query = pets.select().where(pets.c.pet_id == pet_id)
        pet = await database.fetch_one(query)
        if not pet:
            msg = "Pet didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return pet

    @staticmethod
    async def get_by_client_id(client_id: int) -> list[Pet]:
        query = pets.select().where(pets.c.client_id == client_id)
        pets_list = await database.fetch_all(query)
        if not pets_list:
            msg = "Pets didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return pets_list

    async def create(self, pet: CreatePetRequest) -> dict[str, Any]:
        query = pets.insert().values(
            client_id=pet.client_id,
            name=pet.name,
            birthday=pet.birthday)
        last_id = await database.execute(query)
        return {**pet.model_dump(), "pet_id": last_id}

    async def update(self, pet_id: int, item: Pet):
        query = pets.update().where(pets.c.pet_id == pet_id).values(**item.model_dump())
        result = await database.execute(query)
        if not result:
            msg = "Pet didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return pet_id

    async def delete(self, pet_id: int):
        query = pets.delete().where(pets.c.pet_id == pet_id)
        result = await database.execute(query)
        if not result:
            msg = "Pet didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return pet_id
