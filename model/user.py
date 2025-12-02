from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from Base import Base

class User(Base):
    __table__ = 'User'