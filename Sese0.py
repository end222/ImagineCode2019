#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 09:42:13 2019

@author: ubuntelex
"""

import sys, traceback

class User_Answer:
  def __init__(self, rtype, box, num, obj):
    self.rtype = rtype
    self.box = box
    self.num = num
    self.obj = obj

def analyze(v_text):
    """
    Detect the type
    1 - Desde, de
    2 - En, hasta, a
    3 - Error, not recognised
    """

    i = 0
    rtype = 3

    if lang == "es":
        while i < len(v_text):
            if v_text[i] == "desde" or v_text[i] == "de":
                word_pos = i
                box = v_text[word_pos+1]
                rtype = 1
            elif v_text[i] == "hasta" or v_text[i] == "a" or v_text[i] == "en":
                word_pos = i
                box = v_text[word_pos+1]
                rtype = 2

            if v_text[i] in num_es or v_text[i].isdigit():
                num = v_text[i]
                obj = v_text[i+1]

            i += 1

        if v_text[0] == "saltar":
            rtype = 4
            num = 0
            obj = ""
            box = ""

    elif lang == "en":
        while i < len(v_text):
            if v_text[i] == "from":
                word_pos = i
                box = v_text[word_pos+1]
                rtype = 1
            elif v_text[i] == "to":
                word_pos = i
                box = v_text[word_pos+1]
                rtype = 2

            if v_text[i] in num_es or v_text[i].isdigit():
                num = v_text[i]
                obj = v_text[i+1]

            i += 1

        if v_text[0] == "saltar":
            rtype = 4
            num = 0
            obj = ""
            box = ""

    return User_Answer(rtype, box, num, obj)


#LECTURA Y PARSEO 

inicial = open("inicial.txt")
final = open("final.txt")
log = open("Sese0.log","w") 

num_es = [
    "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho",
    "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis",
    "diecisiete", "dieciocho", "diecinueve", "veinte",
    "veintiuno", "veintidós", "veintitrés", "veinticuatro",
    "veintiséis", "veintisiete", "veintiocho", "veintinueve"
]

num_en = [
    "one", "two", "three", "four", "five", "six", "seven", "eight",
    "eleven", "nine", "ten", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "thirty-one", "twenty-two", "twenty-three",
    "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine"
]

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
        sys.exit(1)
        
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
        sys.exit(2)

#TAREAS
i = 0
j = 0
for j in list(range(len(obj_fin))):
    recibido1 = False
    recibido2 = False
    while (recibido1 == False):
        print ("Coge " +num_fin[j]+ " " +obj_fin[j]+".")
        log.write("SISTEMA: Coge " +num_fin[j]+ " " +obj_fin[j]+".\n")
        #Comprobacion
        text = input("Respuesta: ").lower()
        log.write("USUARIO: " + text + "\n")
        text_v = text.split()
        output = analyze(text_v)
        if num_fin[j] == output.num and obj_fin[j].lower() == output.obj and output.rtype == 1:
            recibido1 = True
        elif output.rtype == 4:
            recibido1 = True

        if not recibido1:
            print ("Incorrecto, repito orden.")
    while (recibido2 == False):
        print ("Dejalos en " +pos_fin[j]+".")
        log.write("SISTEMA: Dejalos en " +pos_fin[j]+".\n")
        #Comprobacion
        text = input("Respuesta: ").lower()
        log.write("USUARIO: " + text + "\n")
        text_v = text.split()
        output = analyze(text_v)

        if pos_fin[j] == output.box and output.rtype == 2:
            recibido2 = True
        elif output.rtype == 4:
            recibido2 = True

        if not recibido2:
            print ("Incorrecto repito orden.")
