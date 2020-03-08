import requests
from bs4 import BeautifulSoup
import urllib

def run():
    for i in range(1, 11): #Imagen del 1 al 10
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser') #Generando instancia de Beautifulsoup y parseando el contenido html
        image_container = soup.find(id='comic') #Ubicando la etiqueta id donde esta la imagen

        image_url = image_container.find('img')['src'] #Ubicando la url/src de la imagen
        image_name = image_url.split('/')[-1] #Obteniendo el nombre original de la imagen en la ultima diagonal de la url para guardar la imagen
        print('Descargando la imagen {}'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name) #Python3 Descarga de imágenes
        #urllib.urlretrieve('https:{}'.format(image_url), image_name) #Python2 Descarga de imágenes

if __name__ == "__main__":
    run()