

VISIBLE = 'visible'
annotations = [VISIBLE]

def annotation(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

for annotation in annotations:
    globals()[VISIBLE] = annotation
