import numpy
import pandas as pd
archivo_excel='C:/Users/Estudiante/Documents/EMPLEADOS_BD.xlsx'

datos=pd.read_excel(archivo_excel)
total_salario=sum(datos['Salario'])
salario_maximo=max(datos['Salario'])
salario_minimo=min(datos['Salario'])
cuantos_empleados_hay=len(datos)
promedios_salarios1=total_salario/cuantos_empleados_hay
promedios_salarios2=numpy.mean(datos['Salario'])
eps=total_salario*0.04
pension=total_salario*0.04
total_hombres=len(datos[datos['Genero']=="M"])
total_mujeres=len(datos[datos['Genero']=="F"])


print("el total de los salarios de los empleados es =======>",total_salario)
print("El salario maximo de los empleados es:=====> $",salario_maximo)
print("El salario minimo de los empleados es:=====> $",salario_minimo)
print("cuantos empleados tiene la base de datos:====>",cuantos_empleados_hay)
print("el promedio de los salarios es: $:====>",promedios_salarios1)
print("el promedio de los salarios nro2 es: $:====>",promedios_salarios2)
print("el valor de la eps es: $:====>",eps)
print("el valor de la pension es: $:====>",pension)
print("el totalde hombre es : ====>",total_hombres)
print("el total de mujeres es : ====>",total_mujeres)



import openpyxl

resultados=[('Total salario',total_salario),
            ('Salario maximo',salario_maximo),
            ('salario minimo',salario_minimo),
            ('cantidad empleados',cuantos_empleados_hay),
            ('promedio salario',promedios_salarios1),
            ("el valor a pagar de la eps es ===>",eps),
            ("el valor a pagar de la pension es ===>",pension),
            ("el totalde hombre es : ====>",total_hombres),
            ("el total de mujeres es : ====>",total_mujeres)
            ]
print(resultados)

wb=openpyxl.Workbook()
hoja=wb.active
hoja.append(('Enunciado','Resultados'))
for resultados in resultados:
    hoja.append(resultados)
wb.save('C:/Users/Estudiante/Documents/taller1.xlsx')


