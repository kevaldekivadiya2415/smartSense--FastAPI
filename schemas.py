from pydantic import BaseModel
from fastapi import FastAPI

class Blog(BaseModel):
    title: str
    body : str