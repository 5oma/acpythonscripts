"""
Fuerzas gravitatorias entre dos masas (planetas)

"""
# gravedad

G = 6.67e-11
m1 = 5.97e24
m2 = 1.99e30
r = 1.5e11

result = G * m1 * m2
final = result / r**2
result_saturn = result * 95
final_saturn = result_saturn / ((r * 9.6)**2)
print(final, result)
print(final_saturn, result_saturn)
