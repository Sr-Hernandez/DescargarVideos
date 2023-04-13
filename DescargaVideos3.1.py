import urllib.request
import os
from pytube import YouTube
import emoji
import random
from TikTokApi import TikTokApi
from moviepy.editor import *
import facebook
import requests
import re 

# # Pedir al usuario que ingrese la URL del video
# url = input("Ingrese la URL del video que desea descargar: ")

# # Descargar el video desde la URL
# filename = "video.mp4"
# urllib.request.urlretrieve(url, filename)

# # Pedir al usuario que ingrese la dirección IP del celular
# ip_address = input("192.168.0.171")

# Enviar el video al celular a través de la red WiFi


# ip_address = input("192.168.0.171")

# https://www.youtube.com/watch?v=o3Iup-oisQA

def main():
    url = input("Introduce un link de video: ")
    descargar(url)

def descargar(url) -> None:
    filename = "video.mp4"
    if "youtube" in url:

        # Crear objeto YouTube
        yt = YouTube(url)
        # Obtener la mejor resolución del video
        stream = yt.streams.get_highest_resolution()
          # Descargar el video
        stream.download()
       
        global nombre
        nombre = stream.default_filename
        menu = input("1 Guardar, 2 quitar audio")
        if menu=='1':
        
            print(nombre, " Descargado")
            formato(nombre)
        if menu =='2':
            video = VideoFileClip(nombre)
            video_without_audio = video.without_audio()
            video_without_audio.write_videofile(nombre)
            formato(nombre)

        

    if "tiktok" in url:
        api = TikTokApi()
        # Obtén la información del video por su URL
        # url = 'https://www.tiktok.com/@example/video/1234567890123456789'
        video_id = api.get_video_id(url)
        video_info = api.get_video_by_id(video_id)

        # Descarga el video
        video_url = video_info['itemInfo']['itemStruct']['video']['playAddr']
        response = api.session.get(video_url)
        

        nombre=formato("controlparareturn")
        with open(nombre+".mp4", "wb") as f:
             f.write(response.content)
             nombre = stream.default_filename

    if "facebook" in url:
        descarga_facebook(url)
def formato(nombre):
    
    # nombreB = nombre.replace(" ","") 
    # nombreC = nombreB.replace("#","")
    # nombreF=  emoji.replace_emoji(nombreC, '')
    prefijos = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
    sufijos = ['Force', 'Division', 'Battalion', 'Regiment', 'Company', 'Platoon', 'Squad', 'Unit', 'Brigade', 'Corps', 'Fleet']
    palabra = random.choice(prefijos) + random.choice(sufijos)
    if(nombre=="controlparareturn"):
        palabra = random.choice(prefijos) + random.choice(sufijos)
        return palabra
    
    else:
        os.replace(nombre,palabra+".mp4")



    # transferir(palabra)

def transferir(palabra): 
    
    # urllib.request.urlretrieve(url, filename)
    # command = f"adb connect 192.168.0.171:35211 && adb push {palabra}.mp4 /sdcard/DCIM/Camera"
    # os.system(command)
    main()

def descarga_facebook(video_url):
    video_id = input("1 Guardar, 2 quitar audio")
    video_url = 'https://www.facebook.com/watch/?v=123456789'

    # Expresión regular para buscar el ID del video en la URL
    pattern = r'\/videos\/(\d+)'

    # Buscar el ID del video en la URL utilizando la expresión regular
    match = re.search(pattern, video_url)

   
    # El ID del video se encuentra en el primer grupo de la expresión regular
    # video_id = match.group(1)
    print(f'ID del video: {video_id}')
    access_token ='EAAIrnFZCremoBAMy8AWzV2NLqgxl0KuY74HZCJhcnq8B18oy35J8voZAg7Wjqilh4P9BSlbMVYgDyWZC34PtZBJgPZBaagGVZAqjZA2IAlyQZAAZCqazWR70G5DSZC7ZCOMyrLR6NFc3FKbZAcRoiwIUfLyURg7Vc1SEGVEPTWUzcheohWVtmqf0s1K5DpDHaTVdOt44j8fqrGDiDi092QdAl32TGap0wJZAunz8gZD'
    # ID del video de Facebook que quieres descargar
    
    # Crear un objeto GraphAPI utilizando el token de acceso
    graph = facebook.GraphAPI(access_token)
    # Realizar una solicitud para obtener la URL del video
    video = graph.get_object(id=video_id, fields='source')
    # Descargar el video utilizando la URL obtenida
    video_url = video['source']
    response = requests.get(video_url)
    # Guardar el video en un archivo local
    with open('videoFacebook.mp4', 'wb') as f:
        f.write(response.content)


    # Realizar una solicitud HTTP a la URL del video y obtener la respuesta
    

main()