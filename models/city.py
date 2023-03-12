#!/usr/bin/python3
"""
module for the city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from the BaseModel"""
    state_id = ""
    name = ""
