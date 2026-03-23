# ----------------------------------------------------------------------------------------------------
# CHALLENGES
# ----------------------------------------------------------------------------------------------------

'''
Escribe un programa que muestro por consola (con un print):
* Los números del 1 al 100 (ambos incluidos con un salto de línea entre cada impresión), sustituyendo los siguientes:
    * Múltiplos de 3 por la palabra "fizz"
    * Múltiplos de 5 por la palabra "buzz"
    * Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
'''

def fizz_buzz ():

    for number in range(1, 101):
        if (number % 3 == 0) and (number % 5 == 0):
            print ("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)

print(fizz_buzz())

'''
¿Es un anagrama?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
'''

def anagrama (string1, string2):

    if string1 == string2:
        return False
    elif len(string1) != len(string2):
        return False
    elif sorted(string1) == sorted(string2):
        return True
    else:
        return False
    
print(anagrama("roma", "amor"))    # True
print(anagrama("perro", "repro"))  # True
print(anagrama("hola", "hola"))    # False
print(anagrama("gato", "perro"))   # False