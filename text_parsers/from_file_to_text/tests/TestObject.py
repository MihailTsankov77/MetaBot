import os
from annotations import visible

class TestObject:
    x = 0
    y = 0

    def __init__(self, x):
        self.x = x
    
    def mat(self):
        sda = 0
    
    @visible
    def mat2(self):
        print('mat2')
        a = 0

    @visible
    def _mat2(self):
        print('mat2')
        a = 0

    @visible
    def __mat2(self):
        print('mat2')
        a = 0
