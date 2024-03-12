# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:20:02 2023

@author: Estudiante
"""

from openpyxl import Workbook
from openpyxl.styles import fonts
import time

book = Workbook()
sheet = book.active

sheet['A1']=5
sheet['A2']=10

book.save('prueba_ecxel4.xlsx')
