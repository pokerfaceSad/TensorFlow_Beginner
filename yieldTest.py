# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:44:51 2018

@author: XinYuan
"""
from inspect import isgeneratorfunction
import types

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b, a+b
        n = n + 1
        
for n in fab(5):
    print(n)
    
print(type(fab(5)))  # <class 'generator'>
print(type(fab)) # <class 'function'>
print(isgeneratorfunction(fab)) # True
print(isinstance(fab,types.GeneratorType)) # False
print(isinstance(fab(5),types.GeneratorType)) # True