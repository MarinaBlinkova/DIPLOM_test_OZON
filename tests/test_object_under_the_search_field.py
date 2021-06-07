from pages.ozon_page import OzonPage

def test_visit(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_shops().is_displayed()

def test_get_Top_Fashion(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_Top_Fashion().is_displayed()

def test_get_Premium(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_Premium()[1].is_displayed()

def test_get_Ozon_Express(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_Ozon_Express()[1].is_displayed()

def test_get_Ozon_Card(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_Ozon_Card()[1].is_displayed()

def test_get_LIVE(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_LIVE().is_displayed()

def test_get_sale(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_sale().is_displayed()

def test_get_Ozon_Travel(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_Ozon_Travel()[1].is_displayed()

def test_get_Brands(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_Brands().is_displayed()

def test_get_Certificates(driver):
    ozon_page = OzonPage(driver)
    ozon_page.visit()
    assert ozon_page.get_Certificates().is_displayed()
