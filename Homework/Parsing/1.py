import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep
import json

cookies = {
    'PHPSESSID': 'gkit89g81mhr1bm2d5n62hnobg',
    '51a55dae53577255b792d39bfe1d40ac': '0',
    '_ga_BB3QC8QLF4': 'GS1.1.1698057539.1.1.1698060726.0.0.0',
    '_ga': 'GA1.1.937455389.1698057540',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://zaka-zaka.com/',
    # 'Cookie': 'PHPSESSID=gkit89g81mhr1bm2d5n62hnobg; 51a55dae53577255b792d39bfe1d40ac=0; _ga_BB3QC8QLF4=GS1.1.1698057539.1.1.1698060726.0.0.0; _ga=GA1.1.937455389.1698057540',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
result = {}
for i in range(1, 15):
    print('собираю данный со страницы '+str(i))
    sleep(1)

    response = requests.get('https://zaka-zaka.com/game/new/page'+str(i), cookies=cookies, headers=headers)
    with open('page1.html', 'w', encoding='UTF-8') as f:
        f.write(response.text)
    with open('page1.html', 'r', encoding='UTF-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')
        list2 = soup.find('div', class_='tab-items list2')
        blocks = list2.find_all('a', class_='game-block')
        for block in blocks:
            name = block.find('div', class_='game-block-name').text
            price = block.find('div', class_='game-block-price').text.strip()[0:5]
            result[name] = (price)
with open('result1.json', 'w', encoding='UTF-8') as f:
    json.dump(result, f, indent=4,ensure_ascii=False)