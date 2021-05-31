from config import url
from urllib.parse import urlparse

class OzonPage():
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def visit(self):
        self.driver.get(url)

    def get_shops(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Магазины')]")

    def get_Top_Fashion(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'TOP Fashion')]")

    def get_Premium(self):
        return self.driver.find_elements_by_xpath("//*[contains(text(), 'Premium')]")

    def get_Ozon_Express(self):
        return self.driver.find_elements_by_xpath("//*[contains(text(), 'Ozon Express')]")

    def get_Ozon_Card(self):
        return self.driver.find_elements_by_xpath("//*[contains(text(), 'Ozon Card')]")