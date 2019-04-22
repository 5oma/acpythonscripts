# -*- coding: utf-8 -*-
"""
Stack. A linear data structure
Created on Wed Jan 24 13:21:13 2018

Conforme vamos aprendiendo, las estructuras de datos
aparecen en todas partes. De las estructuras de datos
lineales, el stack (una pila de cosas) se caracteriza
por tener una apertura (al frente o arriba) 
y una base (abajo o atrás). 

Sólo podemos hacer operaciones (añadir o borrar) 
sobre el último elemento. 

Algunos ejemplos de stacks: 
    La pila de platos sucios en un restaurante

Cualquier cosa apilada ordenadamente y diferenciada. 
Una pila de elementos de una misma clase. 
Una pila de elementos de diversa clase. 
    
@author: X010TL
"""

# Implementación de un stack en  una clase
class Stack:
    #Inicializamos nuestro stack utilizando una lista vacía
    def __init__(self):
        self.items = []
    
    #Le asignamos a la clase de nuestro stack los siguientes
    #métodos

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

