from abc import ABC

class Singleton(type, ABC):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        if len(args) > 0 or len(kwargs.keys()) > 0:
            raise Exception("already created")
        return cls._instances[cls]
