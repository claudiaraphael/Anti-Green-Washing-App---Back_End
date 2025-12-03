from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from model.product import Product
from extensions import db  # Importa o db globalmente definido

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())

    products = db.relationship("Product", back_populates="owner")
    comments = db.relationship("Comment", back_populates="author")