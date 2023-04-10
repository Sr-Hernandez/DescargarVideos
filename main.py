from pytube import YouTube
import tkinter as tk
# Introducir la URL del video
# url = "https://www.youtube.com/shorts/5KPlK7xTMgI"

# # Crear objeto YouTube
# yt = YouTube(url)

# # Obtener la mejor resolución del video
# stream = yt.streams.get_highest_resolution()



# # Descargar el vi
# stream.download()



def descargar(url) -> None:
  
    # Crear objeto YouTube
    yt = YouTube(url)
    # Obtener la mejor resolución del video
    stream = yt.streams.get_highest_resolution()
      # Descargar el video
    stream.download()
    nombre= yt.title
    print(nombre, " Descargado")
    main()


def main():
    url = input("Introduce un link de video: ")
    descargar(url)

main()