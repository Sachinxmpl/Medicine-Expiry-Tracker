from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database
from .database import engine
from .crud import check_expiry

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Medicine Expiry Tracker")

@app.post("/medicines/", response_model=schemas.Medicine)
def create_medicine(medicine: schemas.MedicineCreate, db: Session = Depends(database.get_db)):
    return crud.create_medicine(db, medicine)

@app.get("/medicines/", response_model=list[schemas.Medicine])
def read_medicines(db: Session = Depends(database.get_db)):
    medicines = crud.get_medicines(db)
    check_expiry(db) 
    return medicines

@app.get("/medicines/{medicine_id}", response_model=schemas.Medicine)
def read_medicine(medicine_id: int, db: Session = Depends(database.get_db)):
    db_medicine = crud.get_medicine(db, medicine_id)
    if db_medicine is None:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return db_medicine

@app.delete("/medicines/{medicine_id}")
def delete_medicine(medicine_id: int, db: Session = Depends(database.get_db)):
    db_medicine = crud.delete_medicine(db, medicine_id)
    if db_medicine is None:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return {"message": "Medicine deleted"}