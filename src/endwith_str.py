#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2014

@author: anroco

How to know if a python str ends in a given string?

¿Como saber si un str python temina en un string determinado?
'''

#create a str
s = 'Strings are immutable sequences of unicode code points'
print(s)

#the endswith() method verify if the string ends with the defined value
#return True or False.
print(s.endswith('points'))
print(s.endswith('immutable'))
