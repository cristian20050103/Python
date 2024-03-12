# -*-
print("subcidio familar")
hijos=int(input("digite cuantos hijos tiene"))
if (hijos<=2):
    print("valor del subcidio=70000")
    valorsub=70000

    edad=int (input("digite la edad de los hijos"))
    estado_civil=input("digite su estado civil")

    if(edad>=6 and edad<=18):
        print("el subcidio de sus hijos es")
        print("el subcidio x hijo es 10.000 adicionales")
        vlad=10000*hijos
    else:
        print("su hijo no cumple con la edad requerida para recibir el subcidio")
        vlad=0

    if(estado_civil=="viudo"):
        print("recibe 20000 adicionales")
        viudo=20000
    else:
        viudo=0
    sumato=vlad+viudo+valorsub
    print("su subcidio tiene un valor de ====>",sumato)


if((hijos>=3)and(hijos<=5)):
    print("valor del subcidio=90000")
    valorsub2=90000
    edad=int (input("digite la edad de los hijos"))
    estado_civil=input("digite su estado civil")

    if(edad>=6 and edad<=18):
        print("el subcidio de sus hijos es")
        print("el subcidio x hijo es 10.000 adicionales")
        vlad=10000*hijos
    else:
        print("su hijo no cumple con la edad requerida para recibir el subcidio")
        vlad=0

    if(estado_civil=="viudo"):
        print("recibe 20000 adicionales")
        viudo=20000
    else:
        viudo=0
    sumato=vlad+viudo+valorsub2
    print("su subcidio tiene un valor de ====>",sumato)




elif(hijos==6):
    print("el subcidio x hijo es 10.000 adicionales")
    valorsub3=120000
    edad=int (input("digite la edad de los hijos"))
    estado_civil=input("digite su estado civil")

    if(edad>=6 and edad<=18):
        print("el subcidio de sus hijos es")
        print("el subcidio x hijo es 10.000 adicionales")
        vlad=10000*hijos
    else:
        print("su hijo no cumple con la edad requerida para recibir el subcidio")
        vlad=0

    if(estado_civil=="viudo"):
        print("recibe 20000 adicionales")
        viudo=20000
    else:
        viudo=0
    sumato=vlad+viudo+valorsub3
    print("su subcidio tiene un valor de ====>",sumato)

