from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from model.base import Base 

class Comment(Base):
    __tablename__ = 'comment'

    id = Column("pk_comment", Integer, primary_key=True)
    text = Column(String(500))
    author = Column(String(80))
    n_estrela = Column(Integer)
    date_inserted = Column(DateTime, default=datetime.now())
    
    product = Column(Integer, ForeignKey('product.pk_product'), nullable=False)

    def __init__(self, author: str, text: str, n_estrela: int = 0, 
             date_inserted: Union[datetime, None] = None):
    self.author = author
    self.text = text
    self.n_estrela = n_estrela
    if date_inserted:
        self.date_inserted = date_inserted


