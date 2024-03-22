numero=int(input("ingrese el numero"))
contador_digitos = 0
for i in str(numero): # La función str() convierte el número en una cadena de texto,
  # lo cual nos permite contar sobre cada dígito individualmente.  
    contador_digitos +=1 
    print("el numero",numero,"tiene",contador_digitos,"digitos")
