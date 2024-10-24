#practica basica de programacion variable y sus tipos
holis = "texto"
x = 1
mi_variable = 12.2
y=34.4
mi_variable=y+mi_variable

print("\n la primera variable es de tipo:",holis, ", verificamos de nuevo",type(holis),"\n")
print(mi_variable)
holis=2
print ("\n Ahora la clase de holis es: ",type(holis),", con un valor de:", holis,'\n')

#practica de tipo de datos
import random
import math as mt

pi=mt.pi
lista=[5,4,3,2,1]
random.shuffle(lista)
my_v=lista[-1]*pi

print("esta es la lista: ",lista,"\neste es el valor de mi variable: ",my_v)
