from ozon_page import SearchHelper
from Locators import OzonSeacrhLocators


def test_ozon_search(driver):
    ozon_main_page = SearchHelper(driver)
    ozon_main_page.visit()
    ozon_main_page.enter_word("Телефон")
    ozon_main_page.click_on_the_search_button()

    def product_titles(self):
        all_list = self.find_elements(OzonSeacrhLocators.LOCATOR_PRODUCT_TITLES)
        return len(all_list) > 0