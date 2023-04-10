import requests
import time


HEADERS = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
  "Accept": "*/*"
}

def main(url: str) -> str:
  res = requests.get(url, headers=HEADERS)
  return res.text


if __name__ == "__main__":
  seconds = 40
  contador = 1
  while True:
    print(f"Visita #{contador}...")
    main("https://www.tiktok.com/@mexicodrive/video/7220250772951305478?lang=es")
    time.sleep(seconds)
    contador += 1