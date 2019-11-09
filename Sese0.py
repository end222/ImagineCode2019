#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 09:42:13 2019

@author: ubuntelex
"""

#LECTURA Y PARSEO 

inicial = open("inicial.txt")
final = open("final.txt")

pos_ini = []
num_ini = []
obj_ini = []
pos_fin = []
num_fin = []
obj_fin = []

while 1:
    
    ini_text = inicial.readline()
    if not ini_text: break
    ini_text = ini_text.rstrip()
    spl_ini = ini_text.split(";") 
    pos_ini.append(spl_ini[0]) 
    num_ini.append(spl_ini[1])
    obj_ini.append(spl_ini[2])
    
while 1:
    fin_text = final.readline()
    if not fin_text: break
    fin_text = fin_text.rstrip()
    spl_fin = fin_text.split(";")
    pos_fin.append(spl_fin[0]) 
    num_fin.append(spl_fin[1])
    obj_fin.append(spl_fin[2])
   
inicial.close()
final.close()

#CASOS ERROR
    
#1. Numero de productos finales mayores que iniciales 
i = 0
j = 0
for i in list(range(len(obj_ini))):
    suma_fin = 0
    for j in list(range(len(obj_fin))):
        if obj_ini[i] == obj_fin[j]:
            suma_fin = suma_fin + int(num_fin[j])
    print (suma_fin)
    if suma_fin > int(num_ini[i]):
        print("Premo que hay mas " +obj_ini[i]+ " de las que tienes")
        
#2. Objecto final no está en el inicial
i = 0
j = 0
for j in list(range(len(obj_fin))):
    found = False
    for i in list(range(len(obj_ini))):
        if obj_fin[j] == obj_ini[i]: 
            found = True
            break
    if found == False:
        print("Oiga señol que no tenemos " +obj_fin[j]+ ". Que si quiere bolsa")

#TAREAS
i = 0
j = 0
for j in list(range(len(obj_fin))):
    recibido1 = False
    recibido2 = False
    while (recibido1 == False):
        print ("Coge " +num_fin[j]+ " " +obj_fin[j]+".")
        #Comprobacion
        recibido1 = True
        if not recibido1:
            print ("Incorrecto, repito orden.")
    while (recibido2 == False):
        print ("Dejalos en " +pos_fin[j]+".")
        #Comprobacion
        recibido2 = True
        if not recibido2:
            print ("Incorrecto repito orden.")
    
        

