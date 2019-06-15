"""
@author: Project D Section B3
"""
import integrals
import math

def f1(x):
    return x**2+2
def f2(x): 
    return (1-x**2)**0.5

def f3(x): 
    return math.cos(x)
    
def f4(x,y):
    return x**2+y**2
    
    
print( "\n\nUsing the following functions the integral of x**2+2 between 0 & 10 is evaluated\n")
print ("Riemann Left =",integrals.riemann_left(f1, 0, 10, 1000))
