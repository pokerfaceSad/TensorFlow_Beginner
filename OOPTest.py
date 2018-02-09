# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:12:10 2018

@author: XinYuan
"""

class Bird:
    def __init__(self,color,height):
        self.color = color
        self.height = height
        '''
            del self.height 删除属性
        '''
    def fly(self):
        print("flying-------")
        '''私有方法在类内部可以调用'''
        self.__flyHigher()
    def __flyHigher(self):
        print("fly Higher")

bird1 = Bird(color=None,height="175cm")
bird1.fly()
print(bird1.height)
print(bird1)
print(type(bird1))
'''
私有方法不能在类外调用
bird.__flyHigher()
AttributeError: 'Bird' object has no attribute '__flyHigher'
'''
bird2 = Bird("Red",height=None)
bird2.fly()
print(bird2)
print(bird2.height)
del bird2.height
'''
删除bird2的height属性
print(bird2.height) AttributeError: 'Bird' object has no attribute 'height'
'''
