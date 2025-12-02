from pydantic import BaseModel
from typing import Optional, List
from model.product import Product
from schemas.comment import CommentSchema

class ProductSchema(BaseModel):
    """Define produto a ser inserido"""
    name: str = "Nutella"
    barcode: str = "3017624010701"

class ProductBuscaSchema(BaseModel):
    """Define busca por nome"""
    name: str = "Nutella"

class ProductViewSchema(BaseModel):
    """Define produto retornado com comentários"""
    id: int = 1
    name: str = "Nutella"
    barcode: str = "3017624010701"
    total_comments: int = 0
    comments: List[CommentSchema]

class ProductDelSchema(BaseModel):
    """Define resposta de deleção"""
    message: str
    name: str

class ListagemProductsSchema(BaseModel):
    """Define listagem de produtos"""
    products: List[ProductViewSchema]

def apresenta_produto(produto: Product):
    """Serializa produto individual"""
    return {
        "id": produto.id,
        "name": produto.name,
        "barcode": produto.barcode,
        "total_comments": len(produto.comments),
        "comments": [{"text": c.text, "author": c.author} for c in produto.comments]
    }

def apresenta_produtos(produtos: List[Product]):
    """Serializa lista de produtos"""
    return {
        "products": [apresenta_produto(p) for p in produtos]
    }