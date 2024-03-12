# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:19:55 2023

@author: Estudiante
"""

print("menu de ejercicios")
print("1.confirmacion mayor de edad")
print("2.verificacion de contraseña")
print("3.calculadora de division")
print("4.menu de pizzas")
opcion=int(input("Digite la obcion a realizar"))
if(opcion==1):
     print("*******************")
     print("identificador de edad")
     edad=int(input("digite la edad========>"))

     if(edad>=18):
      print("usted es mayor de edad")
     else:
      print("usted es menor de edad")
if(opcion==2):
    print("identificador de contraseña")
    contraseña2=1234
    contraseña=int(input("capture la contraseña"))

    if(contraseña==contraseña2):
        print("ingreso aceptado")
    else:
        print("ingreso denegado")
if(opcion==3):
     print("programa que divida dos numeros")
     nro1=int(input("digite Nro1 ====>"))
     nro2=int(input("digite Nro2 ====>"))
     if(nro2>0)and(nro1>0):
         division=nro1/nro2
         print("la multiplicacion de;",nro1,"/",nro2,"Es igual a ===>",division)   
     else:
         print("no se puede dividir por cero")  
if(opcion==4):
    print("menu de pizas")
    print("1.pizza vegetariana")
    print("2.pizza no vegetarianas")
    opcion=int(input("Digite la obcion a realizar"))
    if (opcion==1):
        print("los ingreddientes de la pizza son ")
        print("1.pimiento")
        print("2.tofu")
        print("3.pimiento y tofu")
        opcion=int(input("Digite la obcion a realizar"))
        if(opcion==1):
            print("su pizza es vegetarina y trae mozarella,tomate y pimiento")
        elif(opcion==2):
            print("su pizza es vegetariana y trae mozarella,tomate y tofu")    
        elif(opcion==3):
            print("su pizza es vegetariana y trae mozarella,tomate y pimiento y tofu")

        
    if(opcion==2):
            print("los ingreddientes de la pizza son ")
            print("1.peperoni")
            print("2.jamon") 
            print("3.salmon") 
            opcion=int(input("Digite la obcion a realizar"))
            if(opcion==1):
             print("su pizza no es vegetarina y trae peperoni,mozarella y tomate ")
            elif(opcion==2):
              print("su pizza no es vegetarina y trae jamon,mozarella y tomate") 
            elif(opcion==3):
             print("su pizza no es vegetarina y trae salmon,mozarella y tomate")
 