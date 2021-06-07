from config import url
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Locators import OzonSeacrhLocators


class OzonPage():
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)


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

    def get_LIVE(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'LIVE')]")

    def get_sale(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Акции')]")

    def get_Ozon_Travel(self):
        return self.driver.find_elements_by_xpath("//*[contains(text(), 'Ozon Travel')]")

    def get_Brands(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Бренды')]")

    def get_Certificates(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Сертификаты')]")

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")


class SearchHelper(OzonPage):

    def enter_word(self, word):
        search_field = self.find_element(OzonSeacrhLocators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(OzonSeacrhLocators.LOCATOR_SEARCH_BUTTON).click()


