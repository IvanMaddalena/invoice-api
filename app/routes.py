from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("/invoices/", response_model=schemas.Invoice)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    return crud.create_invoice(db, invoice)

@router.get("/invoices/", response_model=list[schemas.Invoice])
def read_invoices(db: Session = Depends(get_db)):
    return crud.get_invoices(db)

@router.patch("/invoices/{invoice_id}/pay", response_model=schemas.Invoice)
def mark_invoice_as_paid(invoice_id: int, db: Session = Depends(get_db)):
    return crud.pay_invoice(db, invoice_id)

@router.get("/invoices/by_user/", response_model=list[schemas.Invoice])
def read_invoices_by_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_invoices_by_user(db, user_id)
