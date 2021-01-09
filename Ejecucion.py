#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

#realiza el raspado de todos los lugares donde se tiene registro de clima
aux=0

#apertuda de la base de datos que contine los links hacia lugares donde se tiene registro de clima

f = open("linksFinales.txt", "r")


for linea in f:
    #implime el link del lugar que se va a analizar
    print(linea)
    #imprime un indice para saber el porcentaje de avance del programa
    aux=aux+1
    print(aux)
    
    #realiza una ejecucion del programa que realiza el raspado de datos
    #como parametros 
        #localizacion del compilador de python
        #localizacion del programa de raspado
        #link de pagina a analizar
    os.system ("/home/diego/anaconda3/bin/python3 /home/diego/Descargas/extraDatos.py "+ linea)
f.close()
