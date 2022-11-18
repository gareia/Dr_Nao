# -*- coding: utf-8 -*-
import sys
from _entorno import conectarNao

try:
    naoRed, session = conectarNao() 
    #tts_service=session.service("ALTextToSpeech") # Permite hablar al robot
    #sr_service=session.service("ALSpeechRecognition") # Reconocer sonidos en general
    #memory_service=session.service("ALMemory") # Guardar en memoria los datos reconocidos
    motion_service = session.service("ALMotion")# Permite el movimiento del robot
    motion_service.rest() #sentarse 
    
except Exception as e:
    raise Exception("Ocurrió un error inesperado al conectar con Nao"+ e.message)

sys.exit()
