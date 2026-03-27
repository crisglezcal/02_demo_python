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


"""
La sucessión de Fibonacci:
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores. 
- Ejemplo: 0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci ():

    numbers = []

    number1 = 0
    number2 = 1

    numbers.append(number1)
    numbers.append(number2)

    print(number1)
    print(number2)

    for number in range (2, 51):

        new = number1 + number2
        numbers.append(new)

        number1 = number2
        number2 = new

    return numbers
    
result = fibonacci()

print(result)


"""
¿Es un número primo?
Escribe un programa que se encargue de comprobar si un número es o no primo. Hecho esto, imprime los números primos entre 1 y 100.
"""

def prime():
    primeNumbers = [] 

    for n in range(1, 101):
        if n <= 1:
            continue

        isPrime = True

        for i in range(2, n):
            if n % i == 0:  
                isPrime = False  
                break

        if isPrime:  
            primeNumbers.append(n)  

    return primeNumbers  

result = prime()
print(result)

"""
Invirtiendo cadenas:
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text):
    textLen = len(text)
    reversedText = ""
    for i in range(textLen - 1, -1, -1):
        reversedText += text[i]
    return reversedText

text = "Hola mundo"
print(reverse(text))


'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
'''

"""
Crea una única función que sea capaz de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""

def polygon(poly):

    type = poly["type"]
    base = poly["base"]
    height = poly["height"]

    if type == "triangle":
        area = base * height / 2
    elif type == "square":
        area = base * height
    elif type == "rectangle":
        area = base * height
    else:
        raise ValueError("Tipo de polígono no soportado")

    return area

triangle = {
    "type": "triangle",
    "base": 10,
    "height": 5
}

square = {
    "type": "square",
    "base": 5,
    "height": 5
}

rectangle = {
    "type": "rectangle",
    "base": 15,
    "height": 10
}

# Cálculo e impresión de áreas
print("Área del triángulo:", polygon(triangle))
print("Área del cuadrado:", polygon(square))
print("Área del rectángulo:", polygon(rectangle))