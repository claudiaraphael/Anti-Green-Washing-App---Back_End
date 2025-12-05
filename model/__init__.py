from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importing models
from model.comment import Comment
from model.product import Product
from model.user import User

# create the data base path
db_path = "database/"
# if there is no directory...
if not os.path.exists(db_path):
    # create directory
    os.makedirs(db_path)