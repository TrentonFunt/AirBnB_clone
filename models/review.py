#!/usr/bin/python3
"""
This module contains the Review class definition
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class definition
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
