from pydantic import BaseModel
from datetime import date

class MedicineBase(BaseModel):
    name: str
    expiry_date: date
    quantity: int

class MedicineCreate(MedicineBase):
    pass

class Medicine(MedicineBase):
    id: int

    class Config:
        from_attributes = True