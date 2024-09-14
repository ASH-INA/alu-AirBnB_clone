#!/usr/bin/python3
"""Simple file storage implementation."""

import json
from models.base_model import BaseModel

class FileStorage:
    """Handles storage of models in a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Save objects to JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Reload objects from JSON file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects = json.load(f)
            for key, value in objects.items():
                cls_name = value["__class__"]
                cls = globals()[cls_name]
                FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("** Error loading the JSON file **")

    def delete(self, obj):
        """Delete an object from storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()
        else:
            print("** no instance found **")
