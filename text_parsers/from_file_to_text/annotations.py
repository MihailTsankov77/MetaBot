from enum import Enum

class Annotations(Enum):
    VISIBLE = 'visible'

def annotation_func(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


for annotation in Annotations:
    globals()[annotation] = annotation_func
