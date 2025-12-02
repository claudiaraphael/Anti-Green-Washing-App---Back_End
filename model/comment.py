from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from model.base import Base  # ✅ CORRETO

class Comment(Base):
    __tablename__ = 'comment'

    id = Column("pk_comment", Integer, primary_key=True)
    text = Column(String(500))
    author = Column(String(80))
    n_estrela = Column(Integer)
    date_inserted = Column(DateTime, default=datetime.now())
    
    product = Column(Integer, ForeignKey('product.pk_product'), nullable=False)

    def __init__(self, autor:str, texto:str, n_estrela:int = 0, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Comentário

        Arguments:
            texto: o texto de um comentário.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.autor = autor
        self.texto = texto
        self.n_estrela = n_estrela
        if data_insercao:
            self.data_insercao = data_insercao


