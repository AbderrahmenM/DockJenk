"""
Script.py
====================================
File creatend on 4/6/19 at 4 P.M.
Documentation created by Sphinx2.0.
"""
import platform
from mod import Mod

def confession(your_name):
    """
    Return the most important secret of a person.
    
    Parameters
    ----------
    your_name
        A string indicating the name of the person.
    """
    print("The wise {} loves Python.".format(your_name))

def PythonVersion():
    """
    Return the Python version used by this session.
    """
    print(platform.python_version())

def modulo(FirstInt, SecondInt):
    """
    Return the result of the divison of a by b.
    
    Parameters
    ----------
    FirstInt
        Int indicating the numerator.
    SecondInt
        Int indicating the denominatorur.
    """    
    print(Mod(FirstInt, SecondInt)) 

PythonVersion()
confession("Abderrahmen")
modulo(75, 5)