"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import lxml
driver = webdriver.Firefox()
driver.get('https://store.steampowered.com/')
search = driver.find_element(by='id', value='store_nav_search_term')
search.send_keys('Стратегии')
search.send_keys(Keys.ENTER)
sleep(1)
# button = driver.find_element(by='xpath', value='/html/body/div[1]/div[7]/div[6]/form/div[1]/div/div[1]/div[3]/div/div[3]/a[1]')
# button.click()
for i in range(50):
    sleep(0.5)
    driver.execute_script('window.scrollBy(0, 1070)')
page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
container = soup.find('div', id='search_resultsRows')
list_of_games = soup.find_all('div', class_='responsive_search_name_combined')
result = []
for game in list_of_games:
    name = game.find('span', class_='title').text
    result.append(name)
print('собрали вот сколько игр: ', len(result))
print('вот список игр которые мы собрали: ', result)