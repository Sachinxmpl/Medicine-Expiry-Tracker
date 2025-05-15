from sqlalchemy.orm import Session
from .models import Medicine
from .schemas import MedicineCreate
from datetime import date, timedelta
from .config import settings

def create_medicine(db: Session, medicine: MedicineCreate):
    db_medicine = Medicine(**medicine.dict())
    db.add(db_medicine)
    db.commit()
    db.refresh(db_medicine)
    return db_medicine

def get_medicines(db: Session):
    return db.query(Medicine).all()

def get_medicine(db: Session, medicine_id: int):
    return db.query(Medicine).filter(Medicine.id == medicine_id).first()

def delete_medicine(db: Session, medicine_id: int):
    db_medicine = get_medicine(db, medicine_id)
    if db_medicine:
        db.delete(db_medicine)
        db.commit()
    return db_medicine

def check_expiry(db: Session):
    threshold_date = date.today() + timedelta(days=settings.NOTIFICATION_DAYS)
    expiring_medicines = db.query(Medicine).filter(Medicine.expiry_date <= threshold_date).all()
    for medicine in expiring_medicines:
        print(f"Warning: {medicine.name} expires on {medicine.expiry_date}")
    return expiring_medicines