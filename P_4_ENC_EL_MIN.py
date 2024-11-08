"""programa para encontrar el valor minimo de dos numero"""
#request to user
a,b=map(int,input("por favor ingresa los dos numero: ").split())

#decition 
if a>b:
    print(f"el valor minimmo es: {b}")
else:
    print(f"el valor minimo es: {a}")