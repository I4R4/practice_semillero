"""El siguiente programa pone aprueba la creacion de 
funciones para obtener las operaciones basicas"""

#Definicion de las funciones
def suma(a,b):
    return print(a+b)

def resta(a,b):
    return print(a-b)

def multi(a,b):
    return print(a*b)

def div(a,b):
    return print(a/b)

#solicitud de informacion al usuario
num1=int(input("\nPor favor ingrese los siguientes datos,\nPrimer numero: "))
num2=int(input("Segundo numero: "))

op=int(input("Operaciones dissponibles\n 1.Suma\n 2.Resta\n 3.Multiplicacion\n 4.Division\nIngrese la opcion a ejecutar: "))

#ejecucion del programa
operacion={
    1:suma,
    2:resta,
    3:multi,
    4:div
}
#condi para corregir error de valores y la indeterminacion
if num2>num1 and op==2 :
    print(" El segundo numero es mayor que el primero, operacion no viable...\n Corriga el segundo numero...")
elif num2>num1 and op==4 :
    print(" El segundo numero es mayor que el primero, operacion no viable...\n Corriga el segundo numero...")
else: operacion.get(op)(num1,num2)