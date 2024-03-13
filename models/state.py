#!/usr/bin/python3
"""
This module contains the State class definition
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class definition
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        super().__init__(*args, **kwargs)
