# -*- coding: utf-8 -*-
"""
Interés compuesto

Un programa simple que calcula el
compound interest de una cifra por año.

"""

monto_inicial = 1500  # Monto inicial
tasa = 0.5       # Tasa de interés
nummeses = 12      # Número de meses
mes = 1

while mes <= nummeses:
    monto_inicial = monto_inicial * (1 + tasa)
    print("Mes " + str(mes), monto_inicial)
    mes += 1
