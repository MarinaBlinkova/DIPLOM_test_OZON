from selenium.webdriver.common.by import By


class OzonSeacrhLocators():
    LOCATOR_SEARCH_FIELD = (By.NAME, "search")
    LOCATOR_SEARCH_BUTTON = (By.CSS_SELECTOR, "button.b7j")
    LOCATOR_PRODUCT_TITLES = (By.CLASS_NAME, ".a0c6 a0d a0c9")