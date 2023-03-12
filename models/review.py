#!/usr/bin/python3
"""
module for the review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from the BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
