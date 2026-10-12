from pydantic import BaseModel, Field


class Student(BaseModel):
    roll: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=100)
    marks: float = Field(ge=0, le=100)
    address: str = Field(min_length=1, max_length=200)
    placed: bool
