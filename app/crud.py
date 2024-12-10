from sqlalchemy.orm import Session
from . import models, schemas

def get_mesas(db: Session):
    return db.query(models.Mesa).all()

def create_mesa(db: Session, mesa: schemas.MesaCreate):
    db_mesa = models.Mesa(nome=mesa.nome)
    db.add(db_mesa)
    db.commit()
    db.refresh(db_mesa)
    return db_mesa

def create_pedido(db: Session, pedido: schemas.PedidoCreate, mesa_id: int):
    db_pedido = models.Pedido(**pedido.dict(), mesa_id=mesa_id)
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido