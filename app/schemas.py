from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AduanCreate(BaseModel):
    judul: str
    isi: str
    
class AduanUpdate(BaseModel):
    judul: Optional[str]
    isi: Optional[str]
    
class AduanOut(BaseModel):
    id: int
    judul: str
    isi: str
    status: str
    tingkat_sensitivitas: str
    created_at: datetime

    class Config:
        from_attributes = True
        
class SensitifKataCreate(BaseModel):
    kata: str
    kategori: str  
    
class SensitifKataOut(BaseModel):
    id: int
    kata: str
    kategori: str
    created_at: datetime
    
    class Config:
        from_attributes = True