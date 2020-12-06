from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional


class ProviderDto(BaseModel):
    id: Optional[UUID]
    name: str
    price: float
    billing_period: str
    for_occupation: str
    created: datetime

    class Config:
        orm_mode = True
