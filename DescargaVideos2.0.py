import urllib.request
import os

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



def main():
    url = input("Introduce un link de video: ")
    descargar(url)



def descargar(url):    
    urllib.request.urlretrieve(url, filename)
    command = f"adb connect 192.168.0.171:5555 && adb push {filename} /sdcard/Movies/"
    os.system(command)

main()