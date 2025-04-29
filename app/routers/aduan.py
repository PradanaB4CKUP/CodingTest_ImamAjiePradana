from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response, StreamingResponse
import io
import csv
import json
from sqlalchemy.orm import Session
from app import crud, schemas, database, models


router = APIRouter(
    prefix="/aduan",
    tags=["aduan"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AduanOut)
async def create_aduan(aduan: schemas.AduanCreate, db: Session = Depends(get_db)):
    return crud.create_aduan(db, aduan)

@router.get("/", response_model=list[schemas.AduanOut])
async def list_aduan(status : str = None, sort_by : str = "created_at", db: Session = Depends(get_db)):
    return crud.get_all_aduan(db, status, sort_by)

@router.get("/export")
async def export_aduan(format: str = "json", db: Session = Depends(get_db)):
    aduan_list = db.query(models.Aduan).all()

    if format == "json":
        # Export ke JSON
        data = [
            {
                "id": a.id,
                "judul": a.judul,
                "isi": a.isi,
                "status": a.status,
                "tingkat_sensitivitas": a.tingkat_sensitivitas,
                "created_at": a.created_at.isoformat()
            }
            for a in aduan_list
        ]
        return data

    elif format == "csv":
        # Export ke CSV
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Header CSV
        writer.writerow(["id", "judul", "isi", "status", "tingkat_sensitivitas", "created_at"])
        
        # Isi CSV
        for a in aduan_list:
            writer.writerow([
                a.id,
                a.judul,
                a.isi,
                a.status,
                a.tingkat_sensitivitas,
                a.created_at.isoformat()
            ])
        
        output.seek(0)
        return StreamingResponse(
            iter([output.getvalue()]),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=aduan_export.csv"}
        )

    else:
        raise HTTPException(status_code=400, detail="Format must be 'json' or 'csv'")
    
    
@router.get("/{aduan_id}", response_model=schemas.AduanOut)
async def get_aduan(aduan_id: int, db: Session = Depends(get_db)):
    db_aduan = crud.get_aduan(db, aduan_id)
    if db_aduan is None:
        raise HTTPException(status_code=404, detail="Aduan not found")
    return db_aduan

@router.put("/{aduan_id}", response_model=schemas.AduanOut)
async def update_aduan(aduan_id: int, aduan: schemas.AduanUpdate, db: Session = Depends(get_db)):
    db_aduan = crud.update_aduan(db, aduan_id, aduan)
    if db_aduan is None:
        raise HTTPException(status_code=404, detail="Aduan not found")
    return db_aduan

@router.delete("/{aduan_id}")
async def delete_aduan(aduan_id: int, db: Session = Depends(get_db)):
    db_cekaduan = crud.delete_aduan(db, aduan_id)
    if db_cekaduan is None:
        raise HTTPException(status_code=404, detail="aduan not found")
    return {"message": "aduan is deleted"} 
    # return Response(status_code=204)
    
