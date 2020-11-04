#!/usr/bin/python3
"""
The base class to be inherited from
"""


from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """
    The base model class
    """
    def __init__(self, *args, **kwargs):
        """
        constructor for the object
        """
        if kwargs:
            spt = datetime.strptime
            for key, val in kwargs.items():
                if key == "created_at":
                    self.created_at = spt(val, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = spt(val, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        prints: string representation of object
        """
        output = "[" + self.__class__.__name__ + "] ("
        output += str(self.id) + ") " + str(self.__dict__)
        return output

    def save(self):
        """
        updates the updated time and stores in file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns dictionary containing all key/values
        """
        new_dict = {}
        new_dict.update({"__class__": self.__class__.__name__})
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                new_dict.update({key: val.isoformat()})
            else:
                new_dict.update({key: val})
        return new_dict
