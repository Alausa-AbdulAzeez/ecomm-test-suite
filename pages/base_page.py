# base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            return False
        
        # General util function to extract text
    def get_text(self,element):
        try:
            text = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, element))
            ).text
            return text
        except TimeoutException:
            return False
        
