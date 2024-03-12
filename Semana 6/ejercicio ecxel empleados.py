# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 07:36:25 2023

@author: Estudiante
"""

import numpy
import pandas as pd

archivo_ecxel="C:/Users/Estudiante/Documents/EMPLEADOS_BD.xlsx"
datos=pd.read_excel(archivo_ecxel)
cuantos_empleados_hay=len(datos)
total_hombres=len(datos[datos['Genero']=='M'])
total_mujeres=len(datos[datos['Genero']=='F'])
total_salario=sum(datos['Salario'])
ciudad_bogota=len(datos[datos['Ciudad']=='Bogota'])
ciudad_cali=len(datos[datos['Ciudad']=='Cali'])
ciudad_barranquilla=len(datos[datos['Ciudad']=='Barranquilla'])
ciudad_cucuta=len(datos[datos['Ciudad']=='Cucuta'])
ciudad_medellin=len(datos[datos['Ciudad']=='Medellin'])
ciudad_pasto=len(datos[datos['Ciudad']=='Pasto'])
promedio_edad=round(numpy.mean(datos['Edad']))
estrato1=len(datos[datos['Estrato']==1])
estrato2=len(datos[datos['Estrato']==2])
estrato3=len(datos[datos['Estrato']==3])
estrato4=len(datos[datos['Estrato']==4])
estrato5=len(datos[datos['Estrato']==5])
estrato6=len(datos[datos['Estrato']==6])
porcentaje_bogota=cuantos_empleados_hay/ciudad_bogota
porcentaje_cali=cuantos_empleados_hay/ciudad_cali
porcentaje_pasto=cuantos_empleados_hay/ciudad_pasto
porcentaje_h=(total_hombres/cuantos_empleados_hay*100)
porcentaje_m=(total_mujeres/cuantos_empleados_hay*100)




print("cuantos empleados tiene la base de datos;====$",cuantos_empleados_hay)
print("el total de los hombres es:=====",total_hombres)
print("el total de las mujeres es:====",total_mujeres)
print("el total de los salarios de los empleados es:===$",total_salario)
print("el total de empleados en la ciudad de Bogota es:====",ciudad_bogota)
print("el total de empleados en la ciudad de Cali es:====",ciudad_cali)
print("el total de empleados en la ciudad de Barranquilla es:====",ciudad_barranquilla)
print("el total de empleados en la ciudad de Cucuta es:====",ciudad_cucuta)
print("el total de empleados en la ciudad de Medellin es:====",ciudad_medellin)
print("el total de empleados en la ciudad de Pasto es:====",ciudad_pasto)
print("el total de el promedio de edad es:====>",promedio_edad)
print("el total de empleados de estrato 1 es =====>",estrato1)
print("el total de empleados de estrato 2 es =====>",estrato2)
print("el total de empleados de estrato 3 es =====>",estrato3)
print("el total de empleados de estrato 4 es =====>",estrato4)
print("el total de empleados de estrato 5 es =====>",estrato5)
print("el total de empleados de estrato 6 es =====>",estrato6)
print("el porcentaje de los empleados de bogota es=====>",porcentaje_bogota)
print("el porcentaje de los empleados de cali es=====>",porcentaje_cali)
print("el porcentaje de los empleados de pasto es=====>",porcentaje_pasto)
print("el porcentaje de los empleados hombres es=====>",porcentaje_h)
print("el porcentaje de los empleados hombres es=====>",porcentaje_m)





import openpyxl
wb=openpyxl.Workbook()
resultados=[ ('cantidad empleados',cuantos_empleados_hay),
            ("el total de hombres es de",total_hombres),
            ("el total de mujeres es de",total_mujeres),
            ("el total de los salarios de los empleados es:===$",total_salario),
            ("el total de empleados en la ciudad de Bogota es:====$",ciudad_bogota),
            ("el total de empleados en la ciudad de Cali es:====$",ciudad_cali),
            ("el total de empleados en la ciudad de Barranquilla es:====$",ciudad_barranquilla),
            ("el total de empleados en la ciudad de Cucuta es:====$",ciudad_cucuta),
            ("el total de empleados en la ciudad de Medellin es:====$",ciudad_medellin),
            ("el total de empleados en la ciudad de Pasto es:====$",ciudad_pasto),
            ("el total de el promedio de edad es:====>",promedio_edad),
            ("el total de empleados de estrato 1 es =====>",estrato1),
            ("el total de empleados de estrato 2 es =====>",estrato2),
            ("el total de empleados de estrato 3 es =====>",estrato3),
            ("el total de empleados de estrato 4 es =====>",estrato4),
            ("el total de empleados de estrato 5 es =====>",estrato5),
            ("el total de empleados de estrato 6 es =====>",estrato6),
            ("el porcentaje de los empleados de bogota es=====>",porcentaje_bogota),
            ("el porcentaje de los empleados de Cali es=====>",porcentaje_cali),
            ("el porcentaje de los empleados de Cali es=====>",porcentaje_pasto),
            ("el porcentaje de los empleados hombres es=====>",porcentaje_h),
            ("el porcentaje de los empleados mujeres es=====>",porcentaje_m),
    ]



print(resultados)
hoja=wb.active

hoja.append(('Enunciados','resultados'))
for resultados in resultados:
    hoja.append(resultados)
    wb.save('C:/Users/Estudiante/Documents/Libro21.xlsx')