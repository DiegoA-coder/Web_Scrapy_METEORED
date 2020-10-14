#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#fucniones
    
def guardado(datosLimpios):
    
    #abrimos la tabla
    frame=pd.read_csv('auxx.csv')
    
    #creamoso una table igual para despues concatenar
    frame2=pd.DataFrame([datosLimpios],columns=["Lugar","Hora","Fecha","Indice UV","Algo","Humedad","Nubosidad","Viento_Medio","Presion","Visibilidad","Sensacion Termica","Punto de rocio","Niebla","Viento_racha","Cota Nieve","DirViento"])
    
    #concatenamos
    res=frame.append(frame2,sort=False)
    
    #guardamos
    res.to_csv('auxx.csv', header=True, index=False)
    
def limpieza( datos):
    #limpieza de datos
    fin=[datos[0]]
    fin.append(datos[1])
    fin.append(datos[2])
    #separamos primera linea
    aux= datos[3].split(" FPS: ")
    fin.append(aux[0])
    #primer indice
    if (aux[1] == 'no'):
            fin.append("0")
    else:
        fin.append(aux[1])
    #eliminamos ultimo caracter
    fin.append(datos[4][0:len(datos[3])-1])
    fin.append(datos[5][0:len(datos[4])-1])
    
    #separamos por espacio y guardamos primer token
    fin.append((datos[6].split(" "))[0])
    fin.append((datos[7].split(" "))[0])
    fin.append((datos[8].split(" "))[0])
    fin.append((datos[9].split(" "))[0])
    fin.append((datos[10].split(" "))[0])
    
    #identificamos si es numero o 'no'
    if (datos[11] == 'No'):
            fin.append("0")
    else:
        fin.append(datos[11])
    
    #separamos por espacio
    fin.append((datos[12].split(" "))[0])
    fin.append((datos[13].split(" "))[0])
    
    return fin


#parametros  0:Link   1: Lugar    

#verificacion de parametros
if(len(sys.argv) > 1 ):
    #print ("El nombre del programa es " + sys.argv[0])
    #print ("El primer parámetro es " + sys.argv[1])

    #inicio del programa
    
    #abrimo la pag
    #print("entra****************************************")
    result= requests.get(sys.argv[1])
    
    statusCode=result.status_code
    htmlText=result.text
    
    html=BeautifulSoup(result.text, "html.parser")
    
    #extraemos lugar
    entradas=html.find_all('span',{'class': 'contenedor-miga'})
    lugar=entradas[len(entradas)-1].getText()
    luagar=lugar.split(" ")
    lugar2=luagar[len(luagar)-1]
    
    
    entradas=html.find_all('td',{'class': 'first-column'})

    
    #guardasmos lugar y fecha y hora
    primeracol = [lugar2,time.strftime("%d/%m/%y"),time.strftime("%H:%M:%S") ]
    
    
    #empieza el razpado
    en=entradas[0].find_all('dd', {'class': 'ddD2'})
    aux=0
    for aux2 in  en:
        primeracol.append(aux2.getText())
        
    entradas=html.find_all('td',{'class': 'second-column'})
    en=entradas[0].find_all('dd', {'class': 'ddD2'})
    aux=0
    for aux2 in  en:
        primeracol.append(aux2.getText())
        
    #añadimos viento que esta en otro apartado
    viento=html.find_all('span',{'class': 'datos-viento'})
    viento=viento[0].find_all('strong')
    
    #realizamos limpieza de datos
    #print(primeracol)
    dat=limpieza(primeracol)    
    dat.append(viento[0].getText())
    #guardamos datos
    guardado(dat)
    
    #print ("Raspado exitoso...")
    
else:
    print ("Necesario ejecutar con al menos dos parámetros")
    print ("python programa.py Link Lugar")
    
    
