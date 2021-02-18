from forall.web_selenium import selenium_client
from forall.exceptions import *
from bs4 import BeautifulSoup
import time

url_page = 'https://auto.ru/'

def total_count(proxy, headless=True):
    """
    AUTORU. Ф-ция для полчения числа обьявлений по России

    :param proxy_id:
    :param proxy_ip:
    :param proxy_port:
    :param proxy_login:
    :param proxy_pwd:
    :param proxy_type:
    :param headless:
    :return: { data: { total: int}, error: str, error_message: str}
    """
    error = None
    error_message = None

    client = selenium_client(proxy, headless=headless)
    try:
        client.open_url(url_page)
        client.check_network_trouble()
        region = BeautifulSoup(client.client.page_source).find('span', {'class': 'GeoSelect__title-shrinker'}).get_text()
        if region != 'Любой регион':
            f_el = client.client.find_element_by_xpath("//span[@class='GeoSelect__title-shrinker']")
            client.client.execute_script("arguments[0].click();", f_el)

            client.XpathFindAndClick("//div[@class='GeoSelectPopup__regions']/button")

            client.XpathFindAndClick("//span[contains(text(), 'Сохранить') and @class='Button__text']")
        description = BeautifulSoup(client.client.page_source).find('span', {'class': 'IndexSelector__exclusive-text'}).get_text()
        total = int("".join(description.split(',')[0].split('\xa0')[0:2]))
    except NetworkTrouble as err:
        error = 'network'
        error_message = err
        total = None
    except Exception as err:
        error = 'unknown'
        error_message = err
        total = None

    client.quit_browser()

    return {
        'data': {
            'total': total
        },
        'error': error,
        'error_message': error_message
    }

def marks(proxy, headless=True):
    """
        AUTORU. Ф-ция для получения числа обьявлений по каждой марке

        :param proxy_id:
        :param proxy_ip:
        :param proxy_port:
        :param proxy_login:
        :param proxy_pwd:
        :param proxy_type:
        :param headless:
        :return: {data: [{ name: str, url: str, total: int }], error: str, error_message: str}
    """
    error = None
    error_message = None

    list_mark_dict = []

    client = selenium_client(proxy, headless=headless)
    try:
        client.open_url(url_page)
        client.check_network_trouble()
        region = BeautifulSoup(client.client.page_source).find('span', {'class': 'GeoSelect__title-shrinker'}).get_text()
        if region != 'Любой регион':
            f_el = client.client.find_element_by_xpath("//span[@class='GeoSelect__title-shrinker']")
            client.client.execute_script("arguments[0].click();", f_el)

            client.XpathFindAndClick("//div[@class='GeoSelectPopup__regions']/button")

            client.XpathFindAndClick("//span[contains(text(), 'Сохранить') and @class='Button__text']")
        client.XpathFindAndClick("//div[@class='IndexMarks__show-all-icon']")
        list_marks = BeautifulSoup(client.client.page_source).find('div', {'class': 'IndexMarks__marks-with-counts'}).find_all('a', {'class': 'IndexMarks__item'})
        for one_description_mark in list_marks:
            name_mark = one_description_mark.find('div', {'class': 'IndexMarks__item-name'}).get_text()
            count_mark = int(one_description_mark.find('div', {'class': 'IndexMarks__item-count'}).get_text())
            url_mark = one_description_mark['href']
            list_mark_dict.append(
                {
                    'name': name_mark,
                    'url': url_mark,
                    'total': count_mark
                }
            )
    except NetworkTrouble as err:
        error = 'network'
        error_message = err
    except Exception as err:
        error = 'unknown'
        error_message = err

    client.quit_browser()

    return {
        'data': list_mark_dict,
        'error': error,
        'error_message': error_message
    }

def mark_models(proxy, mark_model_url, headless=True):
    """
        AUTORU. Ф-ция для получения числа обьявлений по каждой модели у данной марки

        :param proxy_id:
        :param proxy_ip:
        :param proxy_port:
        :param proxy_login:
        :param proxy_pwd:
        :param proxy_type:
        :param headless:
        :return: {data: [{ name: str, url: str, total: int }], error: str, error_message: str}
    """

    error = None
    error_message = None

    list_mark_model_dict = []

    client = selenium_client(proxy, headless=headless)
    try:
        client.open_url(mark_model_url)
        client.check_network_trouble()
        region = BeautifulSoup(client.client.page_source).find('span', {'class': 'GeoSelect__title-shrinker'}).get_text()
        if region != 'Любой регион':
            f_el = client.client.find_element_by_xpath("//span[@class='GeoSelect__title-shrinker']")
            client.client.execute_script("arguments[0].click();", f_el)

            client.XpathFindAndClick("//div[@class='GeoSelectPopup__regions']/button")

            client.XpathFindAndClick("//span[contains(text(), 'Сохранить') and @class='Button__text']")
        if BeautifulSoup(client.client.page_source).find('span', {'class': 'Link ListingPopularMMM-module__expandLink'}).get_text().find('Нет в продаже') == -1:
            client.XpathFindAndClick("//span[@class='Link ListingPopularMMM-module__expandLink']")  # если много моделей
        list_models = BeautifulSoup(client.client.page_source).find('div', {'class': 'ListingPopularMMM-module__container PageListing-module__popularMMM'}).find_all('div', {'class': 'ListingPopularMMM-module__item'})
        for one_description_model in list_models:
            name_model = one_description_model.find('a').get_text()
            url_model = one_description_model.find('a')['href']
            total_model = int(one_description_model.find('div').get_text())
            list_mark_model_dict.append(
                {
                    'name': name_model,
                    'url': url_model,
                    'total': total_model
                }
            )
    except NetworkTrouble as err:
        error = 'network'
        error_message = err
    except Exception as err:
        error = 'unknown'
        error_message = err

    client.quit_browser()

    return {
        'data': list_mark_model_dict,
        'error': error,
        'error_message': error_message
    }