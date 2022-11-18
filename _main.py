# -*- coding: utf-8 -*-
import os
import time
import sys
from _conexion import removeAllConn
from _entorno import conectarInternet

try:
    
    removeAllConn()

    internetRed = conectarInternet() 
    time.sleep(1)
    os.system("python3 -m pip install numpy")
    #time.sleep(1)
    #os.system("python pip install qi")
    #time.sleep(1)
    #os.system("python pip install urllib2")

    time.sleep(1)
    removeAllConn()

    #Entorno CON NAO
    from _flujoModulos import fcelular, fresultados, frecomendacion

    #Entorno SIN NAO
    #from _simulacionNao import fcelular, fresultados, frecomendacion

    print("------archivo main-------")

    time.sleep(2)
    cel = fcelular()
    print("cel: "+cel)
    if(len(cel) == 0): raise Exception("El campo celular no ha sido registrado")

    res_list = fresultados()
    print("len(resultados): "+str(len(res_list)))
    if(len(res_list) == 0): raise Exception("No hay resultados registrados")
    res_str = ""
    for rs in res_list:
        res_sin = rs[0].replace(" ", "+")
        res_str += res_sin+":"+str(round(rs[1],3))+" "
    print(res_str)

    rec = frecomendacion()
    print("len(rec): "+str(len(rec)))
    if(len(rec) == 0): raise Exception("No hay recomendación registrada")
    rec_str = rec[0].replace(" ","+")
    print(rec_str)
    
except Exception as e:
    sys.exit("Ocurrió un error inesperado en el archivo _flujoModulos.py: "+ e.message)

try:
    internetRed = conectarInternet()

    time.sleep(1)
    os.system("python3 -m pip install --upgrade pip")
    time.sleep(1)
    os.system("python3 -m pip install selenium")
    time.sleep(1)
    os.system("python3 -m pip install packaging")
    time.sleep(1)
    os.system("python3 -m pip install webdriver_manager")
    time.sleep(1)
    os.system("python3 _wsp.py --celular="+cel+ " -rc "+rec_str+" -rs "+res_str)

    time.sleep(1)
    removeAllConn()

except Exception as e:

    time.sleep(1)
    removeAllConn()
    sys.exit("Ocurrió un error inesperado al enviar mensaje a whatsapp. Archivo _main.py o _wsp.py")

sys.exit()
