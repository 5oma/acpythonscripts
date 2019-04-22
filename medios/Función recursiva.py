# -*- coding: utf-8 -*-
"""

Recursion
Created on Thu Jan 25 11:52:41 2018

Para entender la utilidad de la recursión (función que
se llama a sí misma, usualmente) tenemos que ver
el desarrollo de ejemplos sin recursion que son interesantes.

Like the robots of Asimov, all recursive algorithms must
obey three important laws

1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.

@author: x010
"""

# Resolviendo el problema de sumar los elementos de una lista


def list_sum(num_list):
    # Suma los elementos de una lista
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum


num_list = [1, 3, 5, 7, 9]
print(list_sum(num_list))


def list_sum(num_list):
    # Suma los elementos de una lista de manera recursiva
    # haciendo que la función list_sum se llame a sí misma
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

    
print(list_sum([1 , 3, 5, 7, 9]))
