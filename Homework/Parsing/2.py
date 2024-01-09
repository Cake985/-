"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""
import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep
import json
cookies = {
    'stest201': '0',
    'stest207': 'acc0',
    'stest209': 'ct1',
    'tp_city_id': '38733',
    'PHPSESSID': '21f1139c1bcdd7faf30c104ac84fca58',
    'user_public_id': 'Qhn4Nnr5BkoGb43TgJunCdyBdpcizBCVO%2Feegw4nEBXflx6lxBC3%2FKFQgzPUJxC0',
    'expId': 'PRozp8kCSgK4duzzxjym7w',
    'expVar': '2',
    '_gcl_au': '1.1.452668149.1697798407',
    '_ga_RD4H4CBNJ3': 'GS1.1.1697803314.3.1.1697807391.55.0.0',
    '_ga': 'GA1.2.2053369075.1697798408',
    '_rc_sess': 'e1f5a437-7a5a-4f3a-9ec5-56b3220dba18',
    '_rc_uid': '34e2cfc674c826b57e72915103641803',
    'visitedPagesNumber': '12',
    '_slid': '6532590beb7651844a0cca68',
    'uxs_uid': '0d58d760-6f35-11ee-94ab-e1ffad36b699',
    '_gid': 'GA1.2.294664308.1697798415',
    'tmr_lvid': 'd96c3470ac6d250be582062383e28ad8',
    'tmr_lvidTS': '1697798415068',
    'afUserId': '516664f2-b40a-4ded-b237-1deda33981ab-p',
    'AF_SYNC': '1697798417735',
    'tmr_detect': '1%7C1697806255851',
    '_userGUID': '0:lnyhcdxm:bEGdegO0nx1NPYTqQn4wJ2zp8WQITNdN',
    'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22{%5C%22client_id%5C%22:%5C%22[chat]%20c0a84313dde82e7c8b49%5C%22%2C%5C%22client_token%5C%22:%5C%22d965419e352db8e74542cde361d8f9d4%5C%22}%22}',
    'promo500closed': 'true',
    '_slid_server': '6532590beb7651844a0cca68',
    'pageviewTimer': '6852.079',
    '_slsession': '53870619-239D-42E2-ACBD-8A503DC40059',
    'qrator_ssid': '1697806027.573.4gOFl1PR405h1Cws-5skgmjc6rjs3hshajjo9ujfbodtctgc7',
    'pageviewTimerFired15': 'true',
    'pageviewTimerFired30': 'true',
    'pageviewTimerFired60': 'true',
    'qrator_jsid': '1697806137.287.bPTCHjw1vHHd5jPq-en2q6tnjsp7h7878fesq4ch4jmstt3qu',
    'tp_campaign_url': 'https%3A%2F%2Fsochi.technopark.ru%2Fsmartfony%2F%3Futm_referrer%3Dhttps%253A%252F%252Fsochi.technopark.ru%252Fsmartfony%252F',
    'mindboxDeviceUUID': '5aa00510-6b39-4465-8b4b-a2691f8a3f40',
    'directCrm-session': '%7B%22deviceGuid%22%3A%225aa00510-6b39-4465-8b4b-a2691f8a3f40%22%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://sochi.technopark.ru/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
    # 'Cookie': 'stest201=0; stest207=acc0; stest209=ct1; tp_city_id=38733; PHPSESSID=21f1139c1bcdd7faf30c104ac84fca58; user_public_id=Qhn4Nnr5BkoGb43TgJunCdyBdpcizBCVO%2Feegw4nEBXflx6lxBC3%2FKFQgzPUJxC0; expId=PRozp8kCSgK4duzzxjym7w; expVar=2; _gcl_au=1.1.452668149.1697798407; _ga_RD4H4CBNJ3=GS1.1.1697803314.3.1.1697807391.55.0.0; _ga=GA1.2.2053369075.1697798408; _rc_sess=e1f5a437-7a5a-4f3a-9ec5-56b3220dba18; _rc_uid=34e2cfc674c826b57e72915103641803; visitedPagesNumber=12; _slid=6532590beb7651844a0cca68; uxs_uid=0d58d760-6f35-11ee-94ab-e1ffad36b699; _gid=GA1.2.294664308.1697798415; tmr_lvid=d96c3470ac6d250be582062383e28ad8; tmr_lvidTS=1697798415068; afUserId=516664f2-b40a-4ded-b237-1deda33981ab-p; AF_SYNC=1697798417735; tmr_detect=1%7C1697806255851; _userGUID=0:lnyhcdxm:bEGdegO0nx1NPYTqQn4wJ2zp8WQITNdN; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22{%5C%22client_id%5C%22:%5C%22[chat]%20c0a84313dde82e7c8b49%5C%22%2C%5C%22client_token%5C%22:%5C%22d965419e352db8e74542cde361d8f9d4%5C%22}%22}; promo500closed=true; _slid_server=6532590beb7651844a0cca68; pageviewTimer=6852.079; _slsession=53870619-239D-42E2-ACBD-8A503DC40059; qrator_ssid=1697806027.573.4gOFl1PR405h1Cws-5skgmjc6rjs3hshajjo9ujfbodtctgc7; pageviewTimerFired15=true; pageviewTimerFired30=true; pageviewTimerFired60=true; qrator_jsid=1697806137.287.bPTCHjw1vHHd5jPq-en2q6tnjsp7h7878fesq4ch4jmstt3qu; tp_campaign_url=https%3A%2F%2Fsochi.technopark.ru%2Fsmartfony%2F%3Futm_referrer%3Dhttps%253A%252F%252Fsochi.technopark.ru%252Fsmartfony%252F; mindboxDeviceUUID=5aa00510-6b39-4465-8b4b-a2691f8a3f40; directCrm-session=%7B%22deviceGuid%22%3A%225aa00510-6b39-4465-8b4b-a2691f8a3f40%22%7D',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
result = {}
for i in range(1, 25):
    print('собираю данный со страницы '+str(i))
    sleep(1)
    params = {
        'p': i,
    }

    response = requests.get('https://sochi.technopark.ru/smartfony/', params=params, cookies=cookies, headers=headers)
    with open('page.html', 'w', encoding='UTF-8') as f:
        f.write(response.text)
    with open('page.html', 'r', encoding='UTF-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')
        container = soup.find('div',class_='catalog-listing')
        cards = container.find_all('div',class_='product-card-big__container')
        for card in cards:
            name = card.find('div',class_='product-card-big__name').text.strip()
            price = card.find('div',class_='product-prices__price').text.strip()[0:7]
            new_price = ''
            for i in price:
                if i.isdigit():
                    new_price += i
            result[name] = int(new_price)

with open('result.json', 'w') as f:
    json.dump(result, f, indent=4,ensure_ascii=False)