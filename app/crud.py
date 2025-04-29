from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import Response
from . import models, schemas
from app.utils.deteksi import proses_aduan

def create_aduan(db: Session, aduan: schemas.AduanCreate):
    status, sensitivitas = proses_aduan(aduan.isi, db)
    # tingkat = hitung_sensitif(aduan.isi)
    db_aduan = models.Aduan(
        judul=aduan.judul,
        isi=aduan.isi,
        status=status,
        tingkat_sensitivitas=sensitivitas
    )
    db.add(db_aduan)
    db.commit()
    db.refresh(db_aduan)
    return db_aduan

def get_aduan(db: Session, aduan_id: int):
    return db.query(models.Aduan).filter(models.Aduan.id == aduan_id).first()

def get_all_aduan(db: Session, status: str = None, sort_by: str = "created_at"):
    query = db.query(models.Aduan)
    if status:
        query = query.filter(models.Aduan.status == status)
    if sort_by == "created_at":
        query = query.order_by(models.Aduan.created_at.desc())
    elif sort_by == "tingkat_sensitivitas":
        query = query.order_by(models.Aduan.tingkat_sensitivitas.desc())
    return query.all()

def update_aduan(db: Session, aduan_id: int, aduan: schemas.AduanUpdate):
    db_aduan = db.query(models.Aduan).filter(models.Aduan.id == aduan_id).first()
    if not db_aduan:
        return None
    for var, value in vars(aduan).items():
        if value is not None:
            setattr(db_aduan, var, value)
    
    if aduan.isi:
        from app.utils.deteksi import proses_aduan
        status, sensitivitas = proses_aduan(db_aduan.isi, db)
        db_aduan.status = status
        db_aduan.tingkat_sensitivitas = sensitivitas
        
    db.commit()
    db.refresh(db_aduan)
    return db_aduan

def delete_aduan(db: Session, aduan_id: int):
    db_aduan = db.query(models.Aduan).filter(models.Aduan.id == aduan_id).first()
    if not db_aduan:
        # raise HTTPException(status_code=404, detail="Aduan not found")
        return None
    db.delete(db_aduan)
    db.commit()
    return db_aduan  


def create_sensitif_kata(db: Session, kata: schemas.SensitifKataCreate):
    db_kata = models.SensitifKata(**kata.dict())
    db.add(db_kata)
    db.commit()
    db.refresh(db_kata)
    return db_kata

def get_all_sensitif_kata(db: Session):
    return db.query(models.SensitifKata).all()

def delete_sensitif_kata(db: Session, kata_id: int):
    db_kata = db.query(models.SensitifKata).filter(models.SensitifKata.id == kata_id).first()
    if not db_kata:
        return None
    db.delete(db_kata)
    db.commit()
    return db_kata
    
# kata_sensitif = ['korupsi', 'narkoba', 'pelecehan', 'terorisme']

# def hitung_sensitif(isi: str):
#     tingkat = 0
#     for kata in kata_sensitif:
#         if kata in isi.lower():
#             tingkat += 1
#     if tingkat >= 2:
#         return 'sangat sensitif'
#     elif tingkat == 1:
#         return 'sensitif'
#     else:
#         return 'tidak sensitif'