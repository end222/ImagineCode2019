#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 09:42:13 2019
@author: ubuntelex
"""

au_i = 0

import sys
from gtts import gTTS
from pygame import mixer
import time
import speech_recognition as sr
import json

mixer.init()

SPEECH_JSON=json.dumps({'type': 'service_account','project_id': 'curious-clone-258512','private_key_id': '223d719570d38d5813294e3339aaca1811db6d30','private_key': '-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCu4SZ9kseKsh0a\ngTaIn4zMwenoCNmbEul6HFQiXa5li/vPSolELE31+cqVg3oIBstPoRoyOhzE+y2N\nSbaos/0SoXNLR/he7BmvVn26ecOAruGLPffEQDlNBR+mljvUZcTU8ILdcdAMuQ1H\nNvxokDwV/jiFsJq/LQr+1PIhPq9wZLcz7d6xTTfixn89pZY+VwDrim14PRUBf4ke\nRZ0PkL3amFvHpYt1ByVkvt9wxxAtlqzmDiT9ixnsTpnzm5mbFkmPMOYbkHmFSjfN\naBYVzUxEN2cGDndOwnh0bk2c/2hMI0GEVUfYyc0Su1drW/9OsVo6S5ElTDpMh5GD\no+UpsJ5dAgMBAAECggEAAJR6uiEtR4ex1yiXjMgFir0qMIFR3blxQu8z1RbGTvCf\n14g695n8ljTCYSxsGYu3FHpQqdr7V5Z59fw20M0i4Be6jvKSzTwT8N9uEAjDxyfW\neF/3vS8+xfpDca5alt+IZBZn1UbmJD7yTRzzEqTZiHO2LiLCBlgmitP3QnjS9yH0\n+NpqyIVW4VHXPTPoZP4JU1N458owRI93cuCgG6a+IYdDWTPtJzdXccKiA21jA6Xf\n+ScQuUaf1LGkEZXIX6O/BDob86MNaEWTV18O3hgbAYTxTaNpLFiJd8IJuqnfnNVp\n4sNcIX7VU5gIXSNR53oDv5P+AMWbOT3Bb1j+pcEQBwKBgQDlQR1J8qLk3hexIOIm\nSZJ+8JqY62RlRJe1AvUQlz6Xz40N7hC+qPnHyrLUH85lOBP5tZSNzcycjlTO/YV8\nfINOvhE0xLSpJXxhSDdyvV2QjJpe8jeeRMxTLtgfcBYtp51dTLl6vkmWG+ha57wm\n2ynlpr5UoZzblmenHiggCn8aKwKBgQDDSBURfqsHnvcAXovh+366bGkfMvjBXSUQ\nBVqpQI1LVDEN3nk1HZPy5GiuyhB16vT4emCqjfpDR+IuIkKU7KEugLfWUWKzz0sO\nBdr3oVKXZTqkoKs9RNsGDLWow6F6wZmnxhVn/AE5PLtP75iPlYcwvpgT0nfEWUW7\n1iEAjywNlwKBgQDFVK38R9D0xUKJYa+nmy5w+3Nm6z8Id+lJkpkUxcrH64wTkHZz\nVolh8tTJB/OlZoazKxwKjzlvDIhtfwVWaOqxbaLr0+FZsv2D0yB/MAaIdK4vybgc\nEEX719eJ//XnKF6ov3Dr+Tzn62+uR8fJfl5q4YL04ANfc/AWhjutkLtk7wKBgDbO\nTyNm0mdEJPxUjJuysqFtdZ9M9eWG17UEW6putHj0uwOycYAHuhMMKZkMmswNUg0+\ng0y6pgcl8IOUF+2l76KWe4HJu5LNVbosyISBISXeQjQb55M9dN7gyEcCCJrkJNSi\nUjWp00oWElff3YhGpfd3NkUx520SxPBvqzl19R4nAoGAJYMPnH28S1XfE8eBFuSb\nu3ujBJ7HJmvh0XKMOKQAHezRDXkUwqKfbacfRLwOwQyYhfXqqUwDm3xj7T2NcyI9\nAWeH8Msrap3f6+AVwzwdEw0TN680BMM8xfH67hj4VSTbSzMj+ztytV1NNSN6Yjk3\n5X96o+2uQb6EGjiFMUXmWWI=\n-----END PRIVATE KEY-----\n','client_email': 'angels-of-angela@curious-clone-258512.iam.gserviceaccount.com','client_id': '114472607784801307277','auth_uri': 'https://accounts.google.com/o/oauth2/auth','token_uri': 'https://oauth2.googleapis.com/token','auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs','client_x509_cert_url': 'https://www.googleapis.com/robot/v1/metadata/x509/angels-of-angela%40curious-clone-258512.iam.gserviceaccount.com'})



class User_Answer:
  def __init__(self, rtype, box, num, obj):
    self.rtype = rtype
    self.box = box
    self.num = num
    self.obj = obj

def get_audio_to_text():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        if lang == "es":
            return r.recognize_google_cloud(audio, credentials_json=SPEECH_JSON, language="es-ES")
        else:
            return r.recognize_google_cloud(audio, credentials_json=SPEECH_JSON)
    except sr.UnknownValueError:
        return "Error"
    except sr.RequestError as e:
        return "Error"

def analyze(v_text):
    """
    Detect the type
    1 - Desde, de
    2 - En, hasta, a
    3 - Error, not recognised
    """

    i = 0
    rtype = 3
    num = 0
    obj = ""
    box = ""
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
            elif v_text[i] == "to" or v_text[i] == "on":
                word_pos = i
                box = v_text[word_pos+1]
                rtype = 2

            if v_text[i] in num_en or v_text[i].isdigit():
                num = v_text[i]
                obj = v_text[i+1]

            i += 1

        if v_text[0] == "saltar":
            rtype = 4
            num = 0
            obj = ""
            box = ""

    return User_Answer(rtype, box, num, obj)

#IDIOMA
    
print ("Language:\nEnglish - en\nEspañol - es")

lang = input()

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
        if lang == "es":
            string1 = "Coge " +num_fin[j]+ " " +obj_fin[j]
            if int(num_fin[j]) > 1:
                string1 += "s"
            string1 += "."
        else:
            string1 = "Take " +num_fin[j]+ " " +obj_fin[j]
            if int(num_fin[j]) > 1:
                string1 += "s"
            string1 += "."
        print (string1)
        tts1 = gTTS(string1 , lang=lang)
        tts1.save('audios/TTS' + str(au_i) + '.mp3')
        time.sleep(0.5)
        mixer.music.load('audios/TTS' + str(au_i) + '.mp3')
        au_i += 1
        time.sleep(0.5)
        mixer.music.play()
        time.sleep(2)
        log.write("SISTEMA: "+string1+"\n")
        #Comprobacion
        text = get_audio_to_text()
        print("Has dicho: "+text)
        #text = input("Respuesta: ").lower()
        log.write("USUARIO: " + text + "\n")
        text_v = text.split()
        output = analyze(text_v)
        producto = obj_fin[j].lower()

        # Tener en cuenta que el usuario lo dirá en plural si coge más de 1
        if int(num_fin[j]) > 1:
            producto += "s"
        print(producto)
        print(output.obj)
        print(num_es[int(num_fin[j])-1])
        print(output.num)
        print(str(output.rtype))
        if (lang == "es" and num_es[int(num_fin[j])-1] == output.num) or (lang == "en" and num_en[int(num_fin[j])-1] == output.num) and producto == output.obj and output.rtype == 1:
            recibido1 = True
        elif output.rtype == 4:
            recibido1 = True

        if not recibido1:
            print ("Incorrecto, repito orden.")
    while (recibido2 == False):
        string2 = "Dejalo"
        if int(num_fin[j]) > 1:
            string2 += "s"
        string2 += " en " +pos_fin[j]+"."
        print (string2)
        tts2 = gTTS(string2, lang=lang)
        tts2.save('audios/TTS' + str(au_i) + '.mp3')
        time.sleep(0.5)
        mixer.music.load('audios/TTS' + str(au_i) + '.mp3')
        au_i += 1
        time.sleep(0.5)
        mixer.music.play()
        time.sleep(2)
        log.write("SISTEMA: Dejalos en " +pos_fin[j]+".\n")
        #Comprobacion
        text = get_audio_to_text()
        #text = input("Respuesta: ").lower()
        log.write("USUARIO: " + text + "\n")
        text_v = text.split()
        output = analyze(text_v)
        print(pos_fin[j].lower())
        print(output.box.lower())
        if pos_fin[j].lower() == output.box.lower() and output.rtype == 2:
            recibido2 = True
        elif output.rtype == 4:
            recibido2 = True

        if not recibido2:
            print ("Incorrecto repito orden.")
