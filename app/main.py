from fastapi import FastAPI
from app.routers import aduan, sensitif
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(aduan.router)
app.include_router(sensitif.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Deptech API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
