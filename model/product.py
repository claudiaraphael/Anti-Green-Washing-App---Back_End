from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from model.base import Base


# no flask o modelo de dados é dividido em módulos diferentes para diferentes entidades, diferente da fastAPI


class Product(Base):
    __tablename__ = 'product'

    id = Column("pk_product", Integer, primary_key=True)
    name = Column(String(140), unique=True)
    date_inserted = Column(DateTime, default=datetime.now())
    barcode = Column(Integer, unique=True)
    ## ver outras propriedades do produto na API do Open Food Facts
    # relacionamento do objeto Product com o Comment
    comments = relationship("Comment")

    def __init__(self, name: str, barcode: str,
                 date_inserted: Union[datetime, None] = None):
        """Cria um Product"""
        self.name = name
        self.barcode = barcode
        if date_inserted:
            self.date_inserted = date_inserted

    def adiciona_comentario(self, comentario):
        """Adiciona comentário ao produto"""
        self.comments.append(comentario)

