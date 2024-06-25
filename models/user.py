#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
	__tablename__ = "name"
	email = column(String(128), nullable=false
    password = column(String(128), nullable=false)
    first_name = column(firstname(128), nullable=false)
    last_name = column(lastname(128), nullable=false)
