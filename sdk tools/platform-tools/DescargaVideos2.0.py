import urllib.request
import os
from pytube import YouTube
import emoji
# # Pedir al usuario que ingrese la URL del video
# url = input("Ingrese la URL del video que desea descargar: ")

# # Descargar el video desde la URL
# filename = "video.mp4"
# urllib.request.urlretrieve(url, filename)

# # Pedir al usuario que ingrese la dirección IP del celular
# ip_address = input("192.168.0.171")

# Enviar el video al celular a través de la red WiFi

filename = "video.mp4"
# ip_address = input("192.168.0.171")

# https://www.youtube.com/watch?v=o3Iup-oisQA

def main():
    url = input("Introduce un link de video: ")
    descargar(url)

def descargar(url) -> None:
  
    # Crear objeto YouTube
    yt = YouTube(url)
    # Obtener la mejor resolución del video
    stream = yt.streams.get_highest_resolution()
      # Descargar el video
    stream.download()
    global nombre
    # nombre= yt.title

   
    nombre = stream.default_filename

    print(nombre, " Descargado")
    formato(nombre)

def formato(nombre):
    nombreB = nombre.replace(" ","_") 
    nombreC = nombreB.replace("#","")
    nombreF=  emoji.replace_emoji(nombreC, '')

    os.replace(nombre,nombreF)



    transferir(nombreF)

def transferir(nombre): 
    
    # urllib.request.urlretrieve(url, filename)
    command = f"adb connect 192.168.0.171:35211 && adb push {nombre} /sdcard/DCIM/Camera"
    os.system(command)
    main()

main()