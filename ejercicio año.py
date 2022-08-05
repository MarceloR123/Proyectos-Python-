# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:40:34 2022

@author: LENOVO
"""

año = 2028  #el año que queremos comprobar

if año % 4 != 0: #no divisible entre 4
	print("Falso")
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Verdadero")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("Falso")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print("Verdadero")