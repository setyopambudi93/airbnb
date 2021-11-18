import os
import requests
from bs4 import BeautifulSoup

# headers
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
}


# define url
# url = 'https://www.airbnb.com/s/Indonesia--Bali--Badung-Regency--Kuta--%EC%84%B8%EB%AF%B8%EB%83%91/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Indonesia%2C%20Bali%2C%20Badung%20Regency%2C%20Kuta%2C%20%EC%84%B8%EB%AF%B8%EB%83%91&place_id=ChIJ_8h84N9G0i0R0P2CyvsLAwU&checkin=2020-10-31&checkout=2020-11-06&source=structured_search_input_header&search_type=autocomplete_click'
def images_downloads(url, folder):
    # create directory
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass

    # change directory
    os.chdir(os.path.join(os.getcwd(), folder))
    res = requests.get(url, headers=headers)
    # scraping process
    soup = BeautifulSoup(res.text, 'html.parser')

    # find images
    images = soup.find_all('img')
    # getting image
    for image in images:
        link = image['src']
        name = image['alt']

        # save images
        with open(name.replace(' ', '-').replace('/', '').replace('*', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('writing data: ', name)


# testing
url = 'https://www.airbnb.com/s/Indonesia--Bali--Badung-Regency--Kuta--%EC%84%B8%EB%AF%B8%EB%83%91/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Indonesia%2C%20Bali%2C%20Badung%20Regency%2C%20Kuta%2C%20%EC%84%B8%EB%AF%B8%EB%83%91&place_id=ChIJ_8h84N9G0i0R0P2CyvsLAwU&checkin=2020-10-31&checkout=2020-11-06&source=structured_search_input_header&search_type=autocomplete_click'

images_downloads(url, 'bali_hotel')