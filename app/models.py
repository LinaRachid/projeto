from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base

class Mesa(Base):
    __tablename__ = "mesas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    status = Column(Enum("disponivel", "ocupada", "finalizada", name="status_enum"), default="disponivel")
    pedidos = relationship("Pedido", back_populates="mesa")

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(Text)
    observacoes = Column(Text, nullable=True)
    status = Column(Enum("pendente", "preparando", "entregue", "cancelado", name="pedido_status_enum"), default="pendente")
    mesa_id = Column(Integer, ForeignKey("mesas.id"))
    mesa = relationship("Mesa", back_populates="pedidos")