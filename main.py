import requests
from bs4 import BeautifulSoup
import os

# url = '<enter url>'

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r=requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    j=1
    for image in images:
        link = image['src']
        imgname = str(j)
        with open(imgname + '.jpg', 'wb') as f:
            imgreq = requests.get(link)
            f.write(imgreq.content)
            print('writing: ', imgname)
        j=j+1

imagedown('<enter url>','<folder name>')
