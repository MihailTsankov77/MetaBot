
import re

text = '''
def function():
    print('function')

bob.x = 10

bob.y()

bob.y = function
'''


class Test:
    def __init__(self):
        self._x = 0
    
    def y(self):
        print('y')

    def _y(self):
        print('__y')
    
    def __y(self):
        print('__y')

bob = Test()




print(bob._x)
