# -*- coding: utf-8 -*-
from _conexion import connect,createNewConnection,removeConnection
import time
import qi #para crear la sesión

def conectarNao():
    
    #Ver archivo _auxRedes.txt
    try:
        pathNaoId = '_redNaoId.txt'
        with open(pathNaoId, 'r') as file:
            naoRed = file.read()
            print("Red Nao: "+naoRed)
    except Exception:
        raise Exception("Ocurrió un error al leer el archivo "+pathNaoId)
    
    try:
        pathNaoPass = '_redNaoPass.txt'
        with open(pathNaoPass, 'r') as file:
            naoPass = file.read()
    except Exception:
        raise Exception("Ocurrió un error al leer el archivo "+pathNaoPass)
    

    if(createNewConnection(naoRed, naoRed, naoPass) != 0):
        raise Exception("Error al agregar red "+naoRed)

    time.sleep(3)

    if(connect(naoRed, naoRed) != 0):
        removeConnection(naoRed)
        raise Exception("Error al conectarse a la red "+naoRed)

    print("Espere por favor.. conectando con Nao...\n")

    time.sleep(7)
    
    try:
        
        session = qi.Session()

        pathNaoIp = '_redNaoIp.txt'
        with open(pathNaoIp, 'r') as file:
            naoIp = file.read()
            print("Ip Nao: "+naoIp)

        pathNaoPort = '_redNaoPort.txt'
        with open(pathNaoPort , 'r') as file:
            naoPort  = file.read()

        tcpStr = "tcp://" + naoIp + ":" + str(naoPort)
        print(tcpStr)
        session.connect(tcpStr)

        #!--------------------------------INICIAR SERVICIOS------------------------------------
        """
        tts_service=session.service("ALTextToSpeech") # Permite hablar al robot
        sr_service=session.service("ALSpeechRecognition") # Reconocer sonidos en general
        memory_service=session.service("ALMemory") # Guardar en memoria los datos reconocidos
        motion_service = session.service("ALMotion")# Permite el movimiento del robot
        motion_service.rest() #sentarse 

        #Configuración speech recognition
        sr_service.pause(True)
        sr_service.setLanguage("Spanish")
        sr_service.setAudioExpression(True)
        sr_service.setVisualExpression(True)
        tts_service.setLanguage('Spanish') # Lenguaje para hablar
        tts_service.setVolume(0.5)#Disminuir el volumen a la mitad \\vol=30\\
        tts_service.setParameter("speed",150) #50-400 default=100

        return naoRed,tts_service,sr_service,memory_service,motion_service
        """
        return naoRed, session

    except RuntimeError:
        raise Exception("No se puede conectar a Naoqi con ip \"" + naoIp + "\" y puerto" + str(naoPort))
    except Exception:
        raise Exception("Ocurrió un error inesperado al conectar con Nao")

def conectarInternet():

    #Ver archivo _auxRedes.txt
    try:
        pathInternetId = '_redInternetId.txt'
        with open(pathInternetId, 'r') as file:
            internetRed = file.read()
            print("Red internet: "+internetRed)
    except Exception as e:
        raise Exception("Ocurrió un error al leer el archivo "+pathInternetId)

    try:
        pathInternetPass = '_redInternetPass.txt'
        with open(pathInternetPass, 'r') as file:
            celularPass = file.read()
    except Exception as e:
        raise Exception("Ocurrió un error al leer el archivo "+pathInternetPass)
    
    #!--------------------------------------------------------------------

    if(createNewConnection(internetRed, internetRed, celularPass) != 0):
        raise Exception("Error al agregar red " + internetRed)

    time.sleep(3)

    if(connect(internetRed, internetRed) != 0):
        removeConnection(internetRed)
        raise Exception("Error al conectarse a la red " + internetRed)

    return internetRed
