# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:01:47 2023

@author: Estudiante
"""

def suma():
    print("programa que suma dos numeros")
    nro1=int(input("digite Nro1 ====>"))
    nro2=int(input("digite Nro2 ====>"))
    suma=nro1+nro2
    print("la suma de;",nro1,"+",nro2,"Es igual a ===>",suma)
def resta():
    print("programa que reste dos numeros")
    nro1=int(input("digite Nro1 ====>"))
    nro2=int(input("digite Nro2 ====>"))
    resta=nro1-nro2
    print("la resta de;",nro1,"-",nro2,"Es igual a ===>",resta) 
def multiplicacion():
    print("programa que multiplique dos numeros")
    nro1=int(input("digite Nro1 ====>"))
    nro2=int(input("digite Nro2 ====>"))
    multiplicacion=nro1*nro2
    print("la multiplicacion de;",nro1,"*",nro2,"Es igual a ===>",multiplicacion)
def division():
    print("programa que divida dos numeros")
    nro1=int(input("digite Nro1 ====>"))
    nro2=int(input("digite Nro2 ====>"))
    if(nro2>0):
       division=nro1/nro2
       print("la multiplicacion de;",nro1,"/",nro2,"Es igual a ===>",division)
    else:
        print("no se puede dividir por cero")
def findel():
     print("Fin del programa :)")     
def menu():
    print("**********************")
    print("operacion basicas matematicas")
    print("menu prinsipal")
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")
    print("5.salir")
   
salir = False

while not salir:
    menu()
    print("elige la opcion")
    opcion =int(input("digite la opcion:==>"))
    if(opcion==1):
       suma()
    if(opcion==2):
       resta()   
    if(opcion==3):
        multiplicacion()
    if(opcion==4):
       division()
    if(opcion==5):
        salir = True
    else:
        print("fin")     