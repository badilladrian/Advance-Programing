"""This is to show the Python scope of a
switch: case functionality. Using a dictionary keys values
as already defined functions, then calling the argument for each
and save the result in an Object. As Python only manages Objects
we can identify the object as a function by calling it with ()"""

#definimos funcion 0
def zero():
    return "zero"
#definimos funcion 1 
def one():
    return "one"
#definimos funcion 2
def two():
    return "two"
#definimos el diccionario con las funciones
switcher_dictionary = {
        0: zero,
        1: one,
        2: two
    }
 
#creamos un metodo que elige la funcion y la ejecuta
def numbers_to_strings(argument):
    # Get the function from the diccionary, NA default selection if not found
    func = switcher_dictionary.get(argument, "nothing")
    # Execute the function by adding () to the object
    return func()

#we test the switch scope
print(numbers_to_strings(1))

"""Built-in functions, 
such as help(), min() and print() .

User-Defined Functions (UDFs), 
which are functions that users create to help them out;

Anonymous functions, lambda functions.
--------------------------------------------
A method refers to a function which is part of a class."""

# Define a function plus()
def plus(a,b):
  return a + b
  
# Create a Summation class
class Summation(object):
  def sum(self, a, b): #this is a method
    self.contents = a + b
    return self.contents 

my_object = Summation();
my_object.sum(4,16) 
"""you don’t pass the reference to self in this case because self is the 
parameter name for an implicitly passed argument that refers to the 
instance through which a method is being invoked. 
It gets inserted implicitly into the argument list."""


#we can use multiple return values with tuples as so:
# Define multiplicar
def multiplicar(x,y):
  resultado = (x * y)
  return (resultado, y)

# Llamamos multiplicar que devolvera una 
# tupleta con el resultado y el 2nd numero
result, number = multiplicar(2,9)
#result= 18 and number = 9

# Print number
print(number)

"""Existen diferentes tipos de argumentos para las funciones:
Default: argument=value
Required: argument
Keyword: kwargs**
Variable # """

def restar(e,g=5):
    #el segundo argumento es siempre por default 5
    return (e-g);

print(restar(10)) #el resultado es 5
print(restar(10,4))#igual puedo enviar ambos parametros
print(restar(g=3,e=5))
#puedo definir explicitamente cada arg=parametro y cambiar orden

def sumatoria(*lista_numeros):
    """Esto es un DocString, que va luego de la declaracion de la funcion.
    Aqui se define que hace la funcion, en este caso devuelve el resultado
    de la sumatoria de un # indefinido de argumentos. Esto se logra con el
    asterisco frente al argumento dentro de definicion de la funcion.

    Podemos usar la alternativa:
        total = 0
        for i in args:
            total += i
        return total

    Return:
        la suma de todos los argumentos enviados"""
    return sum(lista_numeros)

print(sumatoria(4,5,7,62,234,65363))
#el resultado es 65675

"""Ahora parte de las funciones de Python
es el metodo main(). Cuando se escribe un script.py
y este se importa como un modulo la funcion main()
se ejecuta automaticamente por el interprete.

To make sure that this doesn’t happen, 
you call the main() function when
 __name__ == '__main__'."""

#El sentido del DocString() 
print(sumatoria.__doc__)


#Ahora vamos a hacer el ejercicio de una funcion
#RECURSIVA
def calc_factorial(numero):
    """This is a recursive function
    to find the factorial x! of an integer"""

    if numero == 1:
        return (1)
    else:
        return (numero * calc_factorial(numero-1))

num=7
print("The factorial of ", num, " is ", calc_factorial(7))		