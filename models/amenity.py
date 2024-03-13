#!/usr/bin/python3
"""
This module contains the Amenity class definition
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class definition
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
