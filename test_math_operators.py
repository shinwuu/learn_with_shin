'''
Shinwuu
Date 06/17/2023

Summary:
This code is to help learn the Jenkins CI/CD Pipeline
Unit Tests are extremely important in the SSDLC

'''
from math_operators import *

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(5,3) == 2

def test_multiply():
    assert multiply(2,3) == 6

def test_divide():
    assert divide(10,5) == 2
