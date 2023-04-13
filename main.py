from pytube import YouTube
import tkinter as tk
from flask import Flask, send_file
import os
import urllib.request

# Introducir la URL del video
# url = "https://www.youtube.com/shorts/5KPlK7xTMgI"

# # Crear objeto YouTube
# yt = YouTube(url)

# # Obtener la mejor resolución del video
# stream = yt.streams.get_highest_resolution()



# # Descargar el vi
# stream.download()

app = Flask(__name__)

@app.route('/dw_video')


def dw_video():
    video_path = nombre # Ruta al video que desea enviar
    return send_file(video_path, mimetype='video/mp4')
   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




def descargar(url) -> None:
  
    # Crear objeto YouTube
    yt = YouTube(url)
    # Obtener la mejor resolución del video
    stream = yt.streams.get_highest_resolution()
      # Descargar el video
    stream.download()
    global nombre
    nombre= yt.title

    print(nombre, " Descargado")
  
    main()
    


def main():
    url = input("Introduce un link de video: ")
    descargar(url)


def rutaVideo(video):
    video_file = video.streams.first().download()
    video_path = os.path.abspath(video_file)
    os.remove(video_file)  # elimina el archivo descargado después de obtener la ruta
    return video_path




main()