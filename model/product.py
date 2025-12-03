# model/product.py
from extensions import db  # Importa o db globalmente definido
from datetime import datetime
from sqlalchemy.orm import relationship
from model.comment import Comment
from extensions import db  # Importa o db globalmente definido

class Product(db.Model):
    __tablename__ = 'product'
    
    # AGORA USAMOS db.Column
    id = db.Column("pk_product", db.Integer, primary_key=True)
    name = db.Column(db.String(140), unique=True)
    barcode = db.Column(db.Integer, unique=True)
    date_inserted = db.Column(db.DateTime, default=datetime.now())
    # ... outros campos

    comments = db.relationship("Comment", backref="product") # Usando db.relationship
    # ... outros métodos