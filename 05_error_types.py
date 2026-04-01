# ----------------------------------------------------------------------------------------------------
# ERROR TYPES
# ----------------------------------------------------------------------------------------------------

# SyntaxError
# print "¡Hola comunidad!"
print("¡Hola comunidad!")

# NameError
# print(language) NameError: name 'language' is not defined
language = "Spanish"
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"] # 0, 1, 2, 3, 4
# print(my_list[5]) IndexError: list index out of range

# ModuleNotFoundError
# import maths ModuleNotFoundError: No module named 'maths'
import math

# AttributeError
# print(math.PI) AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

# KeyError
my_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":"35", 1:"Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) KeyError: 'Apelido'

# TypeError
# print(my_list["Nombre"]) TypeError: list indices must be integers or slices, not str

# ImportError
# from math import PI ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
from math import pi
print(pi)

# ValueError
my_int = int("10")
# my_int = int("10 Años") ValueError: invalid literal for int() with base 10: '10 A�os'
print(type(my_int)) 

# ZeroDivisionError
print(4/2)
# print(4/0) ZeroDivisionError: division by zero