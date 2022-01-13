from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy import engine
from . import schemas , models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()


models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    
    try:
        yield db
    
    finally:
        db.close()



@app.post('/blog')
def create(request: schemas.Blog , db : Session = Depends(get_db)):
    return db