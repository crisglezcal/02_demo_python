# ----------------------------------------------------------------------------------------------------
# LAMBDAS
# ----------------------------------------------------------------------------------------------------

'''
Equivalente en una función:
def suma(first_value, second_value):
    return first_value + second_value

Puede guardarse en una variable, p.e.:
sumar = lambda a, b: a + b
print(sumar(2, 3))  # 5

Estructura lambda:
lambda → indica que es una función
first_value, second_value → parámetros (como en def)
: → separa entrada de salida
first_value + second_value → lo que devuelve automáticamente (sin return)
sum_two_values → guarda la lambda en una variable
'''

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))
