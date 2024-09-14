#!/usr/bin/python3
# City model that inherits from the base model.

from models.base_model import BaseModel

class City(BaseModel):
    """City class for AirBnB"""

    def __init__(self, *args, **kwargs):
        """Initialize a new City"""
        super().__init__(*args, **kwargs)
        self.name = ""
