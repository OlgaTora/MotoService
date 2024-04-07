from datetime import date
from typing import List, Any
from fastapi import APIRouter, Depends
from Seminar_10.clinic.schemas.consultation import Consultation
from Seminar_10.clinic.schemas.consultation import CreateConsultationRequest
from Seminar_10.clinic.services.consults import ConsultationService
from Seminar_10.clinic.services.depends import get_consult_service

router = APIRouter()


@router.get('/get-all-consultations/',
            responses={400: {'description': 'Bad request'}},
            response_model=List[Consultation],
            description='Get all consultation', )
async def get_all_clients(consult_service: ConsultationService = Depends(get_consult_service)) -> List:
    clients = await consult_service.get_all()
    return clients


@router.post('/create-new-consultation/',
             responses={400: {'description': 'Bad request'}},
             response_model=Consultation,
             description='Create consultation', )
async def create_client(new_consultation: CreateConsultationRequest,
                        consult_service: ConsultationService = Depends(get_consult_service)) -> dict[str, Any]:
    result = await consult_service.create(new_consultation)
    return result


@router.get('/get-consultation-by-id/{consultation_id}', responses={400: {'description': 'Bad request'}},
            response_model=Consultation,
            description='Search consultation by id')
async def get_client_by_id(consultation_id: int,
                           consult_service: ConsultationService = Depends(get_consult_service)) -> Consultation:
    result = await consult_service.get_by_id(consultation_id)
    return result


@router.get('/get-consultation-by-date/{consultation_date}', responses={400: {'description': 'Bad request'}},
            response_model=list[Consultation],
            description='Search consultation by id')
async def get_client_by_id(consultation_date: date,
                           consult_service: ConsultationService = Depends(get_consult_service)) -> list[Consultation]:
    result = await consult_service.get_by_date(consultation_date)
    return result


@router.delete('/delete-consultation/{consultation_id}', responses={400: {'description': 'Bad request'}},
               response_model=int,
               description='Delete consultation by id')
async def delete(consultation_id: int, consult_service: ConsultationService = Depends(get_consult_service)) -> int:
    result = await consult_service.delete(consultation_id)
    return result


@router.put('/update-consultation/{consultation_id}', responses={400: {'description': 'Bad request'}},
            response_model=int,
            description='Update consultation by id')
async def update(consultation_id: int, item: Consultation,
                 consult_service: ConsultationService = Depends(get_consult_service)) -> int:
    result = await consult_service.update(consultation_id, item)
    return result
