from functools import reduce

# ----------------------------------------------------------------------------------------------------
# HIGH ORDER FUNCTIONS
# ----------------------------------------------------------------------------------------------------

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))# 8
print(sum_two_values_and_add_value(5, 2, sum_five)) # 12

'''
Llamada: sum_two_values_and_add_one(5, 2, sum_one)
Asignación interna: Python entra en la función y hace estas asignaciones automáticas:
first_value = 5
second_value = 2
f = sum_one  <-- Aquí ocurre la magia
Ahora, dentro de esa función, la letra f es simplemente un apodo (alias) para sum_one
'''

# ----------------------------------------------------------------------------------------------------
# CLOSURES
# ----------------------------------------------------------------------------------------------------

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5)) # 16


# ----------------------------------------------------------------------------------------------------
# BUILT-IT HIGHER ORDER FUNCTIONS (Ya existen en el lenguaje)
# ----------------------------------------------------------------------------------------------------

# MAP

numbers = [2, 5, 10, 21]

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers))) # [4, 10, 20, 42]
print(list(map(lambda number: number *2, numbers))) # [4, 10, 20, 42]

# FILTER

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers))) # 21
print(list(filter(lambda number: number > 10, numbers))) # 21

# REDUCE

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))

'''
A diferencia de map o filter, que pasan los elementos de uno en uno, reduce los pasa de dos en dos para ir "acumulando" un resultado.
¿Qué hace la función sum_two_values?
Es una función de apoyo que:
1. Recibe dos argumentos: El "acumulado" y el "siguiente elemento"
2. Muestra por consola: Imprime ambos valores para que veas el proceso
3. Devuelve la suma: Envía el resultado de vuelta a reduce para que este lo use en la siguiente iteración

Al final de todo el recorrido, reduce devuelve un único valor numérico: la suma total de todos los elementos de la lista. En el ejemplo de [1, 2, 3, 4], el resultado final sería 10.
Lista original -> 2, 5, 10, 21
Lista reduce -> 2, 5, 7, 10, 17, 21, 38 -> 2, 5, 2+5=7, 7, 10, 7+10=17, 17, 21, 17+21=38

'''