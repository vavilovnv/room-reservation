from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_lengh=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_lengh=100)

    @validator('name')
    def check_name(cls, value: str):
        if 0 > len(value) > 100:
            raise ValueError('Неверно задано name')
        return value


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        orm_mode = True


class MeetingRoomUpdate(MeetingRoomBase):
    name: str = Field(..., min_length=1, max_lengh=100)

    @validator('name')
    def check_name(cls, value: str):
        if value is None:
            raise ValueError('Поле name не может быть пустым')
        return value
