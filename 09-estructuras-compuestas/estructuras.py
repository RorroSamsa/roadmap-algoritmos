# estructuras.py
# Archivo para practicar listas anidadas, tuplas y diccionarios en Python.

# 1. Listas anidadas (matriz)
# Crea una lista anidada (matriz) de 3x3. Por ejemplo:
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Luego, muestra el primer elemento de la segunda fila (debería ser 4 en el ejemplo).

matriz = [
    [48, 325, 1],
    [490, 37, 23],
    [33, 484, 1111]
]
print(matriz[1][0])

# 2. Tuplas
# Crea una tupla que contenga tres elementos: nombre (str), edad (int), y país (str).
# Por ejemplo: persona = ("Juan", 25, "Chile")
# Luego, muestra el segundo valor de la tupla (la edad).

listaepica = ("Alfredo Sanchez", 38, "Planeta Vegetta")
print (listaepica[1])

# 3. Diccionarios
# Crea un diccionario con las claves: "nombre", "edad", y "carrera".
# Por ejemplo: estudiante = {"nombre": "Ana", "edad": 22, "carrera": "Ingeniería"}
# Luego:
# - Muestra el valor asociado a la clave "nombre".
# - Muestra todas las claves y valores del diccionario.

listoca2 = {"nombre": "Yano", "edad": "88", "carrera": "ingenieria en aeronautica"}
print(listoca2["nombre"])

print(listoca2.keys())

print(listoca2.values())