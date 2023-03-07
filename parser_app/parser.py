import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt


URL = 'https://www.mashina.kg/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.3.949 Yowser/2.5 Safari/537.36'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='list-item list-label')
    car_search = []

    for item in items:
        try:
            car_search.append(
            {
                'title_url': URL + item.find('a').get('href'),
                'title_text': item.find('div', class_='block title').get_text(),
                'image': URL + item.find('div', class_='image-wrap').find('img').get('src'),
                'price': item.find('div', class_='block price').get_text(),
                'info': item.find('div', class_='block info-wrapper item-info-wrapper').get_text()
            })
        except AttributeError:
            pass
    return car_search

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        car_search = []
        for page in range(0, 1):
            html = get_html(f'https://www.mashina.kg/search/all/', params=page)
            car_search.extend(get_data(html.text))
        print(f'\n{car_search}\n')
    else:
        raise Exception('Parse Error......')


parser()