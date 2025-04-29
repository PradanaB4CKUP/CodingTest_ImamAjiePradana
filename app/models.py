from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.database import Base

class Aduan(Base):
    __tablename__ = "aduan"

    id = Column(Integer, primary_key=True, index=True)
    judul = Column(String, nullable=False)
    isi = Column(Text, nullable=False)
    status = Column(String, nullable=False)
    tingkat_sensitivitas = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
class SensitifKata(Base):
    __tablename__ = "sensitif_kata"

    id = Column(Integer, primary_key=True, index=True)
    kata = Column(String, nullable=False)  
    kategori = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 
