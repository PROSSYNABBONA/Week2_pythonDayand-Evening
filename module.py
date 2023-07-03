import module
#Modules
#A simple calc
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
#we dont imort/call a module within in the same file
#print(module.multiply(1,2))

#importing square root and factorial from the module math
from math import *
print(sqrt(16))
print(factorial(3))
#using alias
import math as mtc
print(mtc.sqrt(13))



