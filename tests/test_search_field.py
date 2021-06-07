from pages.ozon_page import SearchHelper
from pages.Locators import OzonSeacrhLocators


def test_ozon_search(driver):
    ozon_main_page = SearchHelper(driver)
    ozon_main_page.visit()
    ozon_main_page.enter_word("Телефон")
    ozon_main_page.click_on_the_search_button()

    def product_titles(self):
        all_list = self.find_elements(OzonSeacrhLocators.LOCATOR_PRODUCT_TITLES)
        return len(all_list) > 0

def test_check_wrong_input_in_search(driver):
    ozon_main_page = SearchHelper(driver)
    ozon_main_page.visit()
    # Try to enter "смартфон" with English keyboard:
    ozon_main_page.enter_word("ntktajy")
    ozon_main_page.click_on_the_search_button()

    def product_titles(self):
        all_list = self.find_elements(OzonSeacrhLocators.LOCATOR_PRODUCT_TITLES)
        return len(all_list) > 0
