from datetime import date
from typing import Any
from fastapi import HTTPException

from Seminar_10.clinic.logger import logger
from Seminar_10.clinic.repositories.irepository import IRepository
from Seminar_10.clinic.schemas.consultation import Consultation, CreateConsultationRequest
from Seminar_10.clinic.services.db import consultation, database


class ConsultRepository(IRepository):

    async def get_all(self) -> list[Consultation]:
        query = consultation.select()
        consultation_list = await database.fetch_all(query)
        if not consultation_list:
            msg = "Table 'consultations' is empty"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return consultation_list

    async def get_by_id(self, consultation_id: int) -> Consultation:
        query = consultation.select().where(consultation.c.consultation_id == consultation_id)
        consult = await database.fetch_one(query)
        if not consultation:
            msg = "Consultation didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return consult

    async def create(self, new_consultation: CreateConsultationRequest) -> dict[str, Any]:
        query = consultation.insert().values(
            client_id=new_consultation.client_id,
            pet_id=new_consultation.pet_id,
            consultation_date=new_consultation.consultation_date,
            description=new_consultation.description)
        last_id = await database.execute(query)
        return {**consultation.model_dump(), "consultation_id": last_id}

    async def update(self, consultation_id: int, item: Consultation):
        query = consultation.update().where(consultation.c.consultation_id == consultation_id).values(
            **item.model_dump())
        result = await database.execute(query)
        if not result:
            msg = "Consultation didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return consultation_id

    async def delete(self, consultation_id: int):
        query = consultation.delete().where(consultation.c.consultation_id == consultation_id)
        result = await database.execute(query)
        if not result:
            msg = "Consultation didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return consultation_id

    @staticmethod
    async def get_by_date(consultation_date: date) -> list[Consultation]:
        query = consultation.select().where(consultation.c.consultation_date == consultation_date)
        consultations = await database.fetch_all(query)
        if not consultations:
            msg = "Consultations for these date didn't found"
            logger.info(msg)
            raise HTTPException(status_code=404, detail=msg)
        return consultations
