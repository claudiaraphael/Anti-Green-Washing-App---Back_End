from extensions import db
from flask import Flask, jsonify
from flask import render_template
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote
import requests
import os
from dotenv import load_dotenv

from model.user import User
from model.comment import Comment
from model.product import Product

# load environment variables
load_dotenv()

OFF_BASE = os.environ.get('OFF_BASE')
OFF_PRODUCT_NAME = os.environ.get('OFF_API_PRODUCT')
OFF_BARCODE = os.environ.get('OFF_BARCODE')


# Application Factory: create app
def create_app(config_name='development'):
    app = Flask(__name__)

    # db config
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

    with app.app_context():
        # db.create_all() usa os modelos que foram importados acima (model.product, etc.)
        db.create_all()


# TO DO:
# - separate responsibilities in this file into different files: run.py, __init__.py, OFF endpoints, CRUD endpoints


# import ennvironment variables

    # Read Routes
    # 1 - endpoint to check if the server is running


    @app.route('/')
    def homepage():
        return render_template('index.html')
    
    
    # get info from barcode
    @app.route('/scan_barcode')
    def scan_barcode():
        response = db.get('OFF_BARCODE', 200)
        product_data = response.jsonify()
        return product_data
    
    # test barcode route: fail/pass
    






    return app
# Como você já implementou o Application Factory Pattern (create_app) e está usando o Flask-SQLAlchemy, a criação da base de dados e das tabelas é automática na inicialização.

# Open Food Facts API
# criar codigo para consulta de dados na base de dados da API e outro pra Open Food Facts API.
# https://openfoodfacts.github.io/openfoodfacts-server/api/ - documentacao do OFF API


# If you submit the product's nutritional values and category, you'll get the Nutri-Score.
# If you submit the product ingredients, you'll get the NOVA group (about food ultra-processing), additives, allergens, normalized ingredients, vegan, vegetarian…
# If you submit the product's category and labels, you'll get the Eco-Score (a rating of the product's environmental impact)


# Referências

# A API da Open Food Facts opera com base na Open Database License: https://opendatacommons.org/licenses/odbl/1-0/
# The individual contents of the database are available under the Database Contents License(https://opendatacommons.org/licenses/dbcl/1-0/).
# Product images are available under the Creative Commons Attribution ShareAlike license (https://creativecommons.org/licenses/by-sa/3.0/deed.en). They may contain graphical elements subject to copyright or other rights that may, in some cases, be reproduced (quotation rights or fair use).
