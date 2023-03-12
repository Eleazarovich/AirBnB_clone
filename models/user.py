#!/usr/bin/python3
"""
module for the user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from the BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
