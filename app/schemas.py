from pydantic import BaseModel
from typing import List, Optional

# Base para criação de pedidos
class PedidoBase(BaseModel):
    descricao: str
    observacoes: Optional[str] = None

# Esquema usado para criar um pedido
class PedidoCreate(PedidoBase):
    pass

# Esquema usado para retornar pedidos (com campos adicionais)
class Pedido(PedidoBase):
    id: int
    status: str
    mesa_id: int

    class Config:
        from_attributes = True  # Substitui orm_mode

# Base para criação de mesas
class MesaBase(BaseModel):
    nome: str

# Esquema usado para criar uma mesa
class MesaCreate(MesaBase):
    pass

# Esquema usado para retornar mesas (com campos adicionais)
class Mesa(MesaBase):
    id: int
    status: str
    pedidos: List[Pedido] = []

    class Config:
        from_attributes = True  # Substitui orm_mode