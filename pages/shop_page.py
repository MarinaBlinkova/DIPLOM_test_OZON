from config import url

class ShopPage():
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def get_shops(self):
        return self.driver.find_elements_by_xpath("//*[contains(text(), 'Книги')]")
