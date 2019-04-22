# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:23:41 2018

@author: X010TL
"""

def función_mágica(n):
    counter = 1 
    while counter <=2000:
        n = n + 1
        print (n)
        counter = counter + 1

def fracción_capital(w,p): 
    #nos da la fracción de capital que debemos invertir
    #si queremos maximizar nuestro dinero a largo plazo
    w = input("¿Cuánto ganas por cada unidad que inviertes?")
    p = input("¿Cuál es la probabilidad de que ganes tu inversión?")
    fracción = ((p*w)-1+p)/w
    print (fracción) 
    
    
    
    