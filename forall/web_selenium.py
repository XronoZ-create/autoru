from .selenium_wire import webdriver as wire
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from .exceptions import *

class selenium_client():
    def __init__(self, proxy, headless=True):
        self.chrome_options = wire.ChromeOptions()
        if headless == True:
            self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_experimental_option("detach", True)

        self.proxy_type = proxy.replace("//", '').split('@')[0].split(':')[0]

        if self.proxy_type != 'no_proxy':
            self.proxy_options = {
                'proxy': {
                    'https': proxy,
                }
            }
            self.client = wire.Chrome(seleniumwire_options=self.proxy_options, options=self.chrome_options)
        else:
            self.client = wire.Chrome(options=self.chrome_options)
        self.client.scopes = [
            '.*stackoverflow.*',
            '.*github.*'
        ]

    def open_url(self, url):
        self.client.get(url)
        return self.client.page_source

    def get_cookies(self):
        """
        Функция получения куки selenium-а в виде словаря
        :return: dict{'name':'value'}
        """

        self.cookies_list = self.client.get_cookies()
        self.cookies_dict = {}
        for self.cookie in self.cookies_list:
            self.cookies_dict[self.cookie['name']] = self.cookie['value']
        print(self.cookies_dict)
        return self.cookies_dict

    def dict_cookies_to_browser(self, dict_cookies):
        for self.name, self.value in dict_cookies.items():
            self.client.add_cookie({'name':self.name, 'value':self.value})

        self.client.get_cookies()

    def get_htmlpage(self):
        return self.client.page_source

    def quit_browser(self):
        self.client.quit()

    def XpathFindAndClick(self, xpath):
        try:
            self.wait = WebDriverWait(self.client, 1)
            self.element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.f_el = self.client.find_element_by_xpath(xpath)
            self.f_el.click()
        except Exception as err:
            self.f_el = self.client.find_element_by_xpath(xpath)
            self.client.execute_script("arguments[0].click();", self.f_el)

    def check_network_trouble(self):
        if BeautifulSoup(self.client.page_source).find('div', {'id': 'error-information-popup-content'}) != None:
            raise NetworkTrouble()
        else:
            pass