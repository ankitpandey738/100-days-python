'''
Modules:

Definition: Consider a module to be the same as a code library.
            A file containing a set of function you want to include in your application.
            
Examples of python modules: .Math
                            .Random
                            .os
                            .time

help('modules')

'''

#math

import math

math.pi
print(math.pi)

math.e
print(math.e)

math.factorial(5)
print(math.factorial(5))

math.ceil(6.5)
print(math.ceil(6.5))

math.floor(6.9) 
print(math.floor(6.9))

math.sqrt(100)
print(math.sqrt(100))

math.acos
print(math.acos)

#Random Module
import random

#random.randint(1,100)

a = [1,2,3,4,5,6,7]
random.shuffle(a)
print(a)

# time module

import time
print(time.time())

time.ctime()
print(time.ctime())


print("Hello")
time.sleep(5)
print("World")


import os

os.getcwd()
print(os.getcwd())

os.listdir()
print(os.listdir())


# Imp
d = help('modules')
print(d)