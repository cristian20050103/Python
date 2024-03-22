contador = 0
numero=int(input("ingrese el numero"))
for i in range(1, numero,2):
    contador += 1 #con 1 cuenta los valores y con i los suma es el mismo codigo solo que cambia la variable de contador a suma  
print("Cantidad de números del 1 al",numero,"de dos en dos:",contador)
