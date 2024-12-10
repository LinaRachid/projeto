from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base
from .dependencies import get_db

# Criar o banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Servidor FastAPI está rodando!"}

@app.post("/mesas/", response_model=schemas.Mesa)
def create_mesa(mesa: schemas.MesaCreate, db: Session = Depends(get_db)):
    return crud.create_mesa(db, mesa)

@app.get("/mesas/", response_model=list[schemas.Mesa])
def list_mesas(db: Session = Depends(get_db)):
    return crud.get_mesas(db)

@app.post("/mesas/{mesa_id}/pedidos/", response_model=schemas.Pedido)
def create_pedido_for_mesa(mesa_id: int, pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    return crud.create_pedido(db, pedido, mesa_id)