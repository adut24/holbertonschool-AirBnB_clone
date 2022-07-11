#!/usr/bin/python3
"""
    Module that define the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.strptime(v, '%Y-%m-%dT' +
                                '%H:%M:%S.%f'))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return an unofficial string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary"""
        a = self.__dict__.copy()
        a.update({"created_at": self.created_at.isoformat()})
        a.update({"updated_at": self.updated_at.isoformat()})
        a.update({"__class__": self.__class__.__name__})
        return a
