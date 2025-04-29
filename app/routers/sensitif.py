from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter(
    prefix="/sensitif",
    tags=["sensitif"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.SensitifKataOut)
async def create_sensitif(kata: schemas.SensitifKataCreate, db: Session = Depends(get_db)):
    return crud.create_sensitif_kata(db, kata)

@router.get("/", response_model=list[schemas.SensitifKataOut])
async def list_sensitif(db: Session = Depends(get_db)):
    return crud.get_all_sensitif_kata(db)

@router.delete("/{kata_id}")
async def delete_sensitif(kata_id: int, db: Session = Depends(get_db)):
    db_kata = crud.delete_sensitif_kata(db, kata_id)
    if db_kata is None:
        raise HTTPException(status_code=404, detail="Kata sensitif not found")
    return {"message": "Kata sensitif deleted"} 