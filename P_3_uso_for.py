"""Se crea un for que haga la impresion de numero en un rango dado"""

#request to user
num1, step =map(int,input("Ingrese el numero tope de la interacion y el paso a dar: ").split())

print("El rango generado es el siguiente: ")
for x in range (0,num1,step):

    print (x,end=" ")

