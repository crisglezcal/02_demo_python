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