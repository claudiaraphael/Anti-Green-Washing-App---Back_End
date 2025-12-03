from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote
import os
from datetime import datetime

# ====================================================================
# 1. INICIALIZAÇÃO DO FLASK-SQLALCHEMY
# O objeto 'db' é criado globalmente, mas não é vinculado ao 'app' ainda.
# Isso será feito dentro da função create_app.
# ====================================================================
db = SQLAlchemy()

# Importar seus modelos após a definição de 'db'
# ATENÇÃO: Seus modelos AGORA HERDAM DE db.Model (veja o passo 2)
# from model.user import User # <-- Precisa importar 'db'
# from model.product import Product # <-- Precisa importar 'db'
# from model.comment import Comment # <-- Precisa importar 'db'

# Importe seus schemas e logger (assumindo que existem)
# from schemas import ProductSchema, ProductViewSchema, ErrorSchema, ProductBuscaSchema, ProdutoSearchSchema
# from logger import logger 
# Vamos simular os imports para manter o foco na estrutura.

# Simulação de imports de classes não fornecidas
class ProductSchema: pass
class ProductViewSchema: pass
class ErrorSchema: pass
class ProductBuscaSchema: pass
class ProdutoSearchSchema: pass
product_tag = "Produtos"
logger = print 

# ====================================================================
# 2. APPLICATION FACTORY PATTERN: FUNÇÃO CREATE_APP
# ====================================================================
def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Configuração do SQLite e o Engine
    if config_name == 'testing':
        # SQLite em memória para testes (o que você queria!)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
    else:
        # SQLite em arquivo para desenvolvimento/produção
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///antigreenwashing.db' 

    # Configuração padrão do Flask-SQLAlchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Vincula o objeto 'db' ao App (aqui ele pega as configurações)
    db.init_app(app)
    
    # Cria todas as tabelas dentro do contexto da aplicação (AQUI é onde o DB é inicializado)
    with app.app_context():
        db.create_all()

    # TO DO: Mover as rotas para um Blueprint ou 'routes.py' e registrar aqui.
    # Rotas de exemplo (mantidas aqui para demonstração):
    
    @app.route('/')
    def home():
        return "Welcome!"

    @app.post('/add_product', tags=[product_tag],
            responses={"200": ProductViewSchema, "409": ErrorSchema, "400": ErrorSchema}  )
    def add_product(form: ProductSchema):
        """ Adds a new product to the data base """
        
        # Simulação do Product (substitua pela sua classe Product importada)
        class Product(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(140), unique=True)
            barcode = db.Column(db.Integer, unique=True)
            
            def __init__(self, name, barcode):
                self.name = name
                self.barcode = barcode

        # Aqui usamos o db.session do Flask-SQLAlchemy
        session = db.session 
        
        # Assumindo que 'form' tem .name e .barcode
        product = Product(
            name='Test Product', # Substitua por form.name
            barcode=123456789 # Substitua por form.barcode
        )
        logger(f"Adding a product: '{product.name}'")

        try:
            session.add(product)
            session.commit()
            logger(f"Product added successfully: '{product.name}'")
            return jsonify({"message": f"Product {product.name} added"}), 200 # Retorno simulado
        
        except IntegrityError as e:
            session.rollback() # Sempre faça rollback em caso de erro!
            error_msg = "Product is already in the data base"
            logger(f"Error adding '{product.name}': {error_msg}")
            return {"message": error_msg}, 409
        
        except Exception as e:
            session.rollback()
            error_msg = "Could not add the product"
            logger(f"Erro: {error_msg}")
            return {"message": error_msg}, 400

    # ... Adicione suas outras rotas aqui usando @app.route, @app.get, etc. ...
    
    return app


# ====================================================================
# 3. EXECUTANDO A APLICAÇÃO (Bloco principal)
# ====================================================================
if __name__ == '__main__':
    # Cria e executa a aplicação usando a configuração de desenvolvimento
    app = create_app('development')
    app.run(debug=True)