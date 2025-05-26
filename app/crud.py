from sqlalchemy.orm import Session
from app import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def create_invoice(db: Session, invoice: schemas.InvoiceCreate):
    db_invoice = models.Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_invoices(db: Session):
    return db.query(models.Invoice).all()

def pay_invoice(db: Session, invoice_id: int):
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if invoice:
        invoice.paid = True
        db.commit()
        db.refresh(invoice)
    return invoice

def get_invoices_by_user(db: Session, user_id: int):
    return db.query(models.Invoice).filter(models.Invoice.user_id == user_id).all()

