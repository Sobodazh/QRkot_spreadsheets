from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt

from core.config import settings


class DonationCreate(BaseModel):
    full_amount: PositiveInt = Field(..., example=settings.FOR_EXAMPLE)
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationDB(DonationCreate):
    id: int
    create_date: Optional[datetime] = Field(None, example=settings.FROM_TIME)

    class Config:
        orm_mode = True


class DonationDBFull(DonationDB):
    id: int
    create_date: Optional[datetime] = Field(None, example=settings.FROM_TIME)
    user_id: Optional[int]
    invested_amount: Optional[int]
    fully_invested: Optional[bool]
    close_date: Optional[datetime] = Field(None, example=settings.TO_TIME)