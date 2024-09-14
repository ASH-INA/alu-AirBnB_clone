#!/usr/bin/python3
# User model inheriting from the Base model.

from models.base_model import BaseModel

class User(BaseModel):
    """User class for AirBnB"""

    def __init__(self, *args, **kwargs):
        """Initialize a new User"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
