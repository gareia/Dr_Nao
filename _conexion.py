# -*- coding: utf-8 -*-
import os

def createNewConnection(name, SSID, password):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+password+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
    with open(name+".xml", 'w') as file:
        file.write(config)
    return os.system(command)
 
def connect(name, SSID):
    command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
    return os.system(command)

def removeConnection(name):
    os.remove(name+".xml")

def removeAllConn():
    try:
        dir = os.path.dirname(os.path.realpath(__file__))
        print("Directorio actual: " + dir)
        for f in os.listdir(dir):
            if(f[-4:] == ".xml"): 
                xml = os.path.join(dir, f)
                os.remove(xml)
                print("Xml removido: " + xml)

    except Exception:
        raise Exception("Ocurrió un error al momento de eliminar los archivos .xml. Archivo conexion.py")


def displayAvailableNetworks():
    command = "netsh wlan show networks interface=Wi-Fi"
    os.system(command)