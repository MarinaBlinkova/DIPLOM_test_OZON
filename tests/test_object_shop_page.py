from pages.shop_page import ShopPage
from pages.ozon_page import OzonPage
import time

def test_shops(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    ozon_page.get_shops().click()
    time.sleep(5)
    shop_page = ShopPage(driver)
    assert shop_page.get_shops()[1].is_displayed()
    time.sleep(5)