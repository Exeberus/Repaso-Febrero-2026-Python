# Comprensión de Listas.

# Ejemplo
'''
numeros = [1, 4, 5, 8, 9]
numeros_dobles = [i * 2 for i in numeros] #Comprehension

print(numeros_dobles)
'''

# No compresión:
numeros = [1, 4, 5, 8, 9]
numeros_dobles = []

for i in numeros:
    n = i*2
    numeros_dobles.append(n)

print(numeros_dobles)