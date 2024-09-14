#!/usr/bin/python3
# The state model inheriting from the base model.

from models.base_model import BaseModel

class State(BaseModel):
    """State class for AirBnB"""

    def __init__(self, *args, **kwargs):
        """Initialize a new State"""
        super().__init__(*args, **kwargs)
        self.name = ""
