from pydantic import BaseModel

from datetime import date
from decimal import Decimal
from typing import Optional
from enum import Enum


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class Operation(BaseModel):
    id: int
    data: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]

    class Config:
        orm_mode = True


