#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

#realiza el raspado de todos los estados de mexico
aux=0
f = open("linksTotales.txt", "r")
for linea in f:
    print(linea)
    aux=aux+1
    print(aux)
    os.system ("/home/diego/anaconda3/bin/python3 /home/diego/Descargas/extraDatos.py "+ linea)
f.close()
