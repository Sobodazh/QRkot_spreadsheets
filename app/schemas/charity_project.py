from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt, validator

from core.config import settings


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=settings.MIN_LENGHT,
                                max_length=settings.MAX_LENGHT)
    description: Optional[str] = Field(None, min_length=settings.MIN_LENGHT)
    full_amount: Optional[PositiveInt] = Field(None, example=settings.FOR_EXAMPLE)


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=settings.MIN_LENGHT,
                      max_length=settings.MAX_LENGHT)
    description: str = Field(..., min_length=settings.MIN_LENGHT)
    full_amount: PositiveInt = Field(..., example=settings.FOR_EXAMPLE)


class CharityProjectUpdate(CharityProjectBase):
    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя проекта не может быть пустым!')
        return value

    class Config:
        extra = Extra.forbid


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: Optional[int]
    fully_invested: Optional[bool]
    create_date: Optional[datetime] = Field(None, example=settings.FROM_TIME)
    close_date: Optional[datetime] = Field(None, example=settings.TO_TIME)

    class Config:
        orm_mode = True