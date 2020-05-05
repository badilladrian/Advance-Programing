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
#Cada browser necesita su driver

#Se definen las funciones para hacer las pruebas, siempre debe incluir el nombre test_

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(5)
        buscar_por_xpath = driver.find_element_by_xpath(
            "//*[@id='fakebox-input']")
        time.sleep(5)
        buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(3)

#Tear down cierra el objeto/classe

    def tearDown(self):
        self.driver.close()


#xpath es una estructura XML de objetos
#xpath relativo //*[@id="fakebox-input"]

#xpath absoluto

# este es el main para correr las pruebas
if __name__ == '__main__':
    unittest.main()
