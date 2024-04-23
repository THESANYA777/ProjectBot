import requests
from bs4 import BeautifulSoup as bs

from config import bitcoin, ton, usdt, atom, near, sol, matic


# класс для запроса на каждую из криптовалют
class Request:
    def bitcoin_request(self):
        # получение запроса
        r = requests.get(bitcoin)
        # преобразовываем в text
        soup = bs(r.text, 'html.parser')
        # получаем цену
        actual_price = soup.find_all('span', class_='sc-f70bb44c-0 jxpCgO base-text')
        for price in actual_price:
            return price.text  # возвращаем цену со знаком $

    def ton_request(self):
        r = requests.get(ton)
        soup = bs(r.text, 'html.parser')
        actual_price = soup.find_all('span', class_='sc-f70bb44c-0 jxpCgO base-text')
        for price in actual_price:
            return price.text

    def usdt_request(self):
        r = requests.get(usdt)
        soup = bs(r.text, 'html.parser')
        actual_price = soup.find_all('span', class_='sc-f70bb44c-0 jxpCgO base-text')
        for price in actual_price:
            return price.text

    def atom_request(self):
        r = requests.get(atom)
        soup = bs(r.text, 'html.parser')
        actual_price = soup.find_all('span', class_='sc-f70bb44c-0 jxpCgO base-text')
        for price in actual_price:
            return price.text

    def near_request(self):
        r = requests.get(near)
        soup = bs(r.text, 'html.parser')
        actual_price = soup.find_all('span', class_='sc-f70bb44c-0 jxpCgO base-text')
        for price in actual_price:
            return price.text

    def sol_request(self):
        r = requests.get(sol)
        soup = bs(r.text, 'html.parser')
        actual_price = soup.find_all('span', class_='sc-f70bb44c-0 jxpCgO base-text')
        for price in actual_price:
            return price.text

    def matic_request(self):
        r = requests.get(matic)
        soup = bs(r.text, 'html.parser')
        actual_price = soup.find_all('span', class_='sc-f70bb44c-0 jxpCgO base-text')
        for price in actual_price:
            return price.text
