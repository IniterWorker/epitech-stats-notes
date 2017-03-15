from abc import ABCMeta
from abc import abstractmethod
import json
import os
import errno


class JSONSD:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __serialize__(self):
        raise NotImplemented

    @abstractmethod
    def __deserialize__(self, obj):
        raise NotImplemented


class JSONPO:

    def __init__(self, path):
        if not isinstance(path, str):
            raise TypeError("The path isn't a string type")
        self.path = path

    def load(self, obj):
        if not isinstance(obj, JSONSD):
            raise TypeError("The Object need to inherent of JSON(SD).")
        if not os.path.exists(os.path.dirname(self.path)):
            try:
                os.makedirs(os.path.dirname(self.path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        if os.path.exists(self.path):
            with open(self.path) as f:
                obj.__deserialize__(json.load(f))
        else:
            self.save(obj)

    def save(self, obj):
        if not isinstance(obj, JSONSD):
            raise TypeError("The Object need to inherent of JSON(SD).")
        if not os.path.exists(os.path.dirname(self.path)):
            try:
                os.makedirs(os.path.dirname(self.path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        with open(self.path, 'w+') as f:
            f.write(obj.__serialize__().__str__())
