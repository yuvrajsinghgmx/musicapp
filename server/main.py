from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
app= FastAPI ()

DATABASE_URL ='postgresql://postgres:sigma@postgres@localhost:5433/musicapp'

engine =create_engine(DATABASE_URL)

sessionLocal = sessionmaker()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str



@app.post('/signup')
def singup_user(user:UserCreate):
    print(user.name)
    print(user.email)
    print(user.password)


    pass