# Comprensión de Listas.

# Ejemplo.

# No compresión:
'''
numeros = [1, 4, 5, 8, 9]
numeros_dobles = []

for i in numeros:
    n = i*2
    numeros_dobles.append(n)

print(numeros_dobles)
'''

'''# Comprensión
numeros = [1, 2, 3, 4, 5, 8, 9]
numeros_dobles = [i * 2 for i in numeros] #Comprehension

print(numeros_dobles)

menor_4 = [i if (i < 4) else '*' for i in numeros]
print(menor_4)'''

## Practica

numeros_practica_tp1 = [3, 7, 10, 15, 20]
numeros_mayores_10_tp1 = [n * 3  for n in numeros_practica_tp1 if (n > 10)]

print(numeros_mayores_10_tp1)

numeros_practica_tp2 = [1, 2, 3, 4, 5]
numeros_impar_o_par_tp2 = ['Par' if (i % 2 == 0) else 'Impar' for i in numeros_practica_tp2]

print(numeros_impar_o_par_tp2)