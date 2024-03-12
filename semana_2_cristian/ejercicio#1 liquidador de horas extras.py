# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:25:06 2023

@author: Estudiante
"""
print("liquidador de horas extras")
nombre=input("Digite el nombre del empleador")
salario=int(input("digite el salario empleador"))
dias=30
laborados=int(input("digitete los dias laborados"))
nrodiurna=float(input("Digite Nro. horas extras diurnas"))
nronocturna=float(input("Digite Nro. horas extras nocturnas"))
nrodiafestivos=float(input("Digite Nro. horas extras diurnas festivos"))
nronochefestivos=float(input("Digite Nro. horas nocturnas festivos"))
horas_extras=(((salario/240)*nrodiurna)*1.25)+(((salario/240)*nronocturna)*1.75)+(((salario/240)*nronochefestivos)*2)+(((salario/240)*nronochefestivos)*2.5)
basico=(salario/dias)*laborados
if (salario<= 2320000):
    subsidio=140606/30*laborados
else:
    subsidio=0

print(nombre)
print(salario)
print("el salario basicos es:>>>> $",basico)
print("el subsidio de trasnporte es:=====$",subsidio)
print("el valor por pagar por horas extras es: $",horas_extras)
print("neto a pagar",basico+horas_extras)
print("***********************************")



