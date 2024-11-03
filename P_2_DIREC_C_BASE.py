"""El siguiente programa tendra un directorio 
para la almacenar informacion y consultar"""

#Definicion del directorio
direc={"1005483290":15,"1005483295":22,"49734619":60}

#Interaccion consulta usuario
consul=input("Introduce un documento para consultar: ")

#validacion en la base del direcctorio
if consul in direc:
    print("La edad de "+ consul +" es " +str(direc[consul]))
else:
    edad=int(input("El documento no esta cargado, introduce la edad: ")) #adicion en caso de que el documento no este
    direc[consul]=edad
    print("Agregado exitosamente a la base")
    print(direc)
