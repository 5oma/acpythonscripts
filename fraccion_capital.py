# -*- coding: utf-8 -*-
"""
fracción_capital()
nos da la fracción de capital que debemos invertir
si queremos maximizar nuestro dinero a largo plazo
Created on Wed Jan 17 09:23:41 2018
@author: X010TL
"""

def fraccion_capital(): 
    "Esta función calcula la fracción del capital que podemos invertir."
    w = int(input("¿Cuánto ganas por cada unidad que inviertes?"))
    p = float(input("¿Cuál es la probabilidad de que ganes tu inversión?"))
    fraccion = (p*w)-1+p
    frac = fraccion/w
    print ("Debes invertir " + str(frac) + " de tu capital.") 
    
    
    
    