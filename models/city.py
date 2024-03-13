#!/usr/bin/python3
"""
This module contains the City class definition
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class definition
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
