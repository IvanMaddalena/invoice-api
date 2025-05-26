from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class User(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True

class InvoiceCreate(BaseModel):
    amount: float
    user_id: int

class Invoice(BaseModel):
    id: int
    amount: float
    paid: bool
    user_id: int
    class Config:
        orm_mode = True
 
