#modules- already written codes by other people which can be used by importing them
#there are 3 types of modules- built in modules also called as standard(which are already included with python), and external modules called as python package index-PyPI(can be donloaded using pip), and those which you write yourself
#The basic way to use a module is to add import module_name at the top of your code, and then using module_name.var to access functions and values with the name var in the module.
#Some of the standard library's useful modules include string, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.
'''import random

for i in range(5):
    value = random.randint(1, 6)
    print(value)'''

#There is another kind of import that can be used if you only need certain functions from a module.
#These take the form from module_name import var, and then var can be used as if it were defined normally in your code.
'''from math import pi,sqrt
print (pi)
n=25
print(sqrt(n))'''

#You can import a module or object under a different name using the as keyword.
from math import sqrt as square_root
print(square_root(100))