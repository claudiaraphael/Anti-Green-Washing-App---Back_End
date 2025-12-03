# app.py (Final)

from flask import Flask, jsonify
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote
import os

# ====================================================================
# 1. IMPORTS E VINCULAÇÕES
# ====================================================================

# Importa o objeto 'db' não-vinculado
from extensions import db 

# Importa todos os modelos. Isso é CRUCIAL para que db.create_all() os encontre.
import model.product
import model.user
import model.comment

# Importações de Schemas e Logger (mantidas como stubs para o exemplo)
class ProductSchema: pass
class ProductViewSchema: pass
class ErrorSchema: pass
class ProdutoSearchSchema: pass
class ProductDelSchema: pass
class ProductBuscaSchema: pass
product_tag = "Produto"
logger = print 

# ====================================================================
# 2. APPLICATION FACTORY: FUNÇÃO CREATE_APP
# ====================================================================
def create_app(config_name='development'):
    app = Flask(__name__)
    
    # ------------------ Configuração do DB ------------------
    if config_name == 'testing':
        # SQLite em memória para testes (ISOLAMENTO!)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
    else:
        # SQLite em arquivo (Desenvolvimento/Produção)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///antigreenwashing.db' 

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # VINCULA o objeto 'db' ao App (com as configurações acima)
    db.init_app(app)
    
    # CRIA AS TABELAS: Precisa estar dentro do contexto da aplicação
    with app.app_context():
        # db.create_all() usa os modelos que foram importados acima (model.product, etc.)
        db.create_all()

    # ------------------ 3. ROTAS (Endpoints) ------------------
    
    @app.route('/')
    def home():
        return "Welcome!"

    @app.post('/add_product', tags=[product_tag],
            responses={"200": ProductViewSchema, "409": ErrorSchema, "400": ErrorSchema}  )
    def add_product(form: ProductSchema):
        """ Adds a new product to the data base """
        
        # Agora você importa o Product no topo (from model.product import Product) e o usa aqui!
        from model.product import Product 
        
        product = Product(name='Test Product', barcode=12345) 

        try:
            # Usando a session gerenciada pelo Flask-SQLAlchemy
            db.session.add(product)
            db.session.commit()
            return jsonify({"message": f"Product {product.name} added"}), 200
        
        except IntegrityError as e:
            db.session.rollback() # ✅ Essencial em caso de erro
            error_msg = "Product is already in the data base"
            return {"message": error_msg}, 409
        
        except Exception as e:
            db.session.rollback()
            return {"message": "Could not add the product"}, 400

    # ... ADICIONE SUAS OUTRAS ROTAS AQUI (get_produto, del_produto, etc.) ...
            
    return app


# ====================================================================
# 4. EXECUÇÃO
# O bloco principal chama o App Factory para iniciar a aplicação
# ====================================================================
if __name__ == '__main__':
    # Inicia a aplicação no modo de desenvolvimento, usando o arquivo antigreenwashing.db
    app = create_app('development')
    app.run(debug=True)