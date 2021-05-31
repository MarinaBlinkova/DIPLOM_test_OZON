import pytest
from selenium import webdriver
from config import url
import time
@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome('C:/Users/Dom/chromedriver_win32/chromedriver.exe')
   driver.set_window_size(1500, 1000)
   driver.implicitly_wait(5)

   yield driver
   driver.quit()