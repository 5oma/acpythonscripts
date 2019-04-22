# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:12:48 2017

@author: yo
"""


import itertools

matrix = list(itertools.combinations([1,2,3,4,5,6,7,8,9,10,11,12], 3))



for item in matrix :
    for element in item:
        element_list.append(element)



def list_sum(matrix):
    #Suma los elementos de una lista
    for i in matrix:
        for j in i:
            the_sum = 0
            the_sum = the_sum + j
        return the_sum
    print(the_sum)






print(list_sum([1,3,5,7,9]))
