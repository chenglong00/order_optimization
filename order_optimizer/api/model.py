from typing import List

from pydantic import BaseModel, constr


class Contact(BaseModel):
    name: constr(max_length=64)
    start: int
    duration: int
    price: int


class OptimizedResult(BaseModel):
    income: str
    path: List[str]


class ErrorResult(BaseModel):
    error_message: str
    error_code: str
