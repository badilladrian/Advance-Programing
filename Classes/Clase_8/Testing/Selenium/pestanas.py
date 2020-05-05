import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):

    #Inicializador
    def setup(self):
        self.driver = webdriver.Chrome(
            executable_path=
            r"C:\Users\badil\Documents\Work\Python\Practice\Selenium\Drivers\chromedriver.exe"
        )

    def test_cambiar_venta(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://stackoverflow.com")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(4)

    if __name__ == '__main--':
        unittest.main()
