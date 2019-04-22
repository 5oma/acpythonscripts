# -*- coding: utf-8 -*-
"""
The random package in numpy
Created on Wed Jan 24 11:39:22 2018

@author: yo
"""

import numpy.random as npr

#Generar un float aleatorio entre 0 y 1
random_number = npr.random_sample()
print (random_number)


#Generar un int aleatorio dados los parámetros
random_int = npr.randint(1,234566789 +1)
print(random_int)

#Arroja una permutación aleatoria de una secuencia dada
lista = list(range(12))
random_permute = npr.permutation(lista)
print(random_permute)


lista = ["Idea", "Amor", "Conciencia", "Fuerza", "Armonía"]
random_permute = npr.permutation(lista)
print(random_permute)



