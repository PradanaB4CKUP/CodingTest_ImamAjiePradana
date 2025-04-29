import re
from sqlalchemy.orm import Session
from app.models import SensitifKata

THRESHOLD_BERBAHAYA = 3

def proses_aduan(isi: str, db: Session):
    daftar_kata = db.query(SensitifKata).all()
    jumlah_kata_terdeteksi = 0
    kategori_ditemukan = []
    
    for item in daftar_kata:
        # pattern = r'\b' + re.escape(item.kata.lower()) + r'\b'
        # if re.search(pattern, isi.lower()):
        #     jumlah_kata_terdeteksi += 1
        #     kategori_ditemukan.append(item.kategori)
        pattern = r'\b' + re.escape(item.kata.lower()) + r'\b'
        matches = re.findall(pattern, isi.lower())  # cari semua kecocokan
        jumlah_kata_terdeteksi += len(matches)  # tambah jumlah kemunculan
        
        print(f"Kata: {item.kata}, Jumlah Matches: {len(matches)}")
        
        if matches:
            kategori_ditemukan.append(item.kategori)
    
    print(f"Jumlah Kata Terdeteksi: {jumlah_kata_terdeteksi}")
    print(f"Kategori Ditemukan: {kategori_ditemukan}")
    
    if jumlah_kata_terdeteksi == 0:
        status = "diproses"
        sensitivitas = "tidak sensitif"
    
    elif jumlah_kata_terdeteksi >= THRESHOLD_BERBAHAYA:
        status = "berbahaya"
        sensitivitas = ", ".join(set(kategori_ditemukan))
    
    else:
        status = "Perlu Review"
        sensitivitas = ", ".join(set(kategori_ditemukan))
    
    return status, sensitivitas