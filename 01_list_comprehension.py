# ----------------------------------------------------------------------------------------------------
# LIST COMPREHENSION
# ----------------------------------------------------------------------------------------------------

# LISTAS "COMPRIMIDAS" → forma corta de crear listas automáticamente

# Creamos una lista normal escrita a mano
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list) # Imprime la lista tal cual la hemos escrito

# Creamos una lista usando list comprehension
my_list = [i for i in range(7)] # "i for i in range(7)" → recorre números del 0 al 6 y los guarda
print(my_list) # [0, 1, 2, 3, 4, 5, 6]

# range(8) genera números del 0 al 7 (el 8 no se incluye)
my_range = range(8)

# Convertimos el range a lista para poder verla
print(list(my_range)) # [0, 1, 2, 3, 4, 5, 6, 7]

# Creamos una lista sumando 1 a cada número
my_list = [i + 1 for i in range(8)] # i va de 0 a 7 → i + 1 da de 1 a 8
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

# Multiplicamos cada número por 2
my_list = [i * 2 for i in range(8)]
print(my_list) # [0, 2, 4, 6, 8, 10, 12, 14]

# Multiplicamos cada número por sí mismo (cuadrado)
my_list = [i * i for i in range(8)]
print(my_list) # [0, 1, 4, 9, 16, 25, 36, 49]

# Definimos una función que suma 5 a un número
def sum_five(number):
    return number + 5 

# Aplicamos la función a cada número de 0 a 7 = sum_five(0), sum_five(1), ..., sum_five(7)
my_list = [sum_five(i) for i in range(8)]
print(my_list) # [5, 6, 7, 8, 9, 10, 11, 12]