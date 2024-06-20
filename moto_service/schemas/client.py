from datetime import date
from typing import Optional

from pydantic import BaseModel


class CreateClientRequest(BaseModel):
    #table name
    document: Optional[str] = None
    surname: str
    firstname: Optional[str] = None
    birthday: Optional[date] = None
    comment: Optional[str] = None


class Client(CreateClientRequest):
    client_id: int

