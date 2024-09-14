#!/usr/bin/python3
# Place model that inherits from the base model.

from models.base_model import BaseModel

class Place(BaseModel):
    """Place class for AirBnB"""

    def __init__(self, *args, **kwargs):
        """Initialize a new Place"""
        super().__init__(*args, **kwargs)
        self.name = ""
