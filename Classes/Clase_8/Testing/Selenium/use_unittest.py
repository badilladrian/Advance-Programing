import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class first_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=
            r"C:\Users\badil\Documents\Work\Python\Practice\Selenium\chromedriver.exe"
        )

    def test_buscar(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        elemento = driver.find_element_by_name("q")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontro el elemento:" not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
