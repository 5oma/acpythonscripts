# -*- coding: utf-8 -*-
"""
Linear search on a sorted list

Created on Fri Dec  8 21:57:26 2017

@author: X010TL
"""



lista = list(range(23,23456345))
target =int(input("Qué número buscas: "))
    
i = 0
while i < len(lista):
    if lista[i] == target:
        print("target encontrado en: ", i + 1)
        break
    else:
        i = i +1
        
            





