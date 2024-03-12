# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:27:24 2023

@author: Estudiante
"""

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