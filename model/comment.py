from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union
from model.product import Product
from extensions import db  # Importa o db globalmente definido

class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column("pk_comment", db.Integer, primary_key=True)
    text = db.Column(db.String(500))
    author = db.Column(db.String(80))
    n_estrela = db.Column(db.Integer)
    date_inserted = db.Column(db.DateTime, default=datetime.now())
    
    product = db.Column(db.Integer, db.ForeignKey('product.pk_product'), nullable=False)

    def __init__(self, author: str, text: str, n_estrela: int = 0, 
             date_inserted: Union[datetime, None] = None):
        self.author = author
        self.text = text
        self.n_estrela = n_estrela
        if date_inserted:
            self.date_inserted = date_inserted


