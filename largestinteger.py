# -*- coding: utf-8 -*-
"""
Linear search on a sorted list

Created on Fri Dec  8 21:57:26 2017

@author: X010TL
"""



lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
target = 8 
    
i = 0
while i < len(lista):
    if lista[i] == target:
        print("target found at:", i + 1)
    else:
        print("item not found")
            





