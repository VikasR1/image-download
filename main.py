import requests
from bs4 import BeautifulSoup
import os

# url = 'https://www.airbnb.co.in/s/ljublijana/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&date_picker_type=flexible_dates&checkin=2022-10-10&checkout=2022-10-11&source=structured_search_input_header&search_type=filter_change'

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

imagedown('https://www.airbnb.co.in/s/Bali--Indonesia/homes?tab_id=home_tab&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&date_picker_type=flexible_dates&checkin=2022-10-10&checkout=2022-10-11&source=structured_search_input_header&search_type=unknown&query=Bali%2C%20Indonesia&price_filter_num_nights=1&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJoQ8Q6NNB0S0RkOYkS7EPkSQ','bali')
