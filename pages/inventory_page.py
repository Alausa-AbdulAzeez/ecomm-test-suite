from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class InventoryPage:
    URL = "https://www.saucedemo.com/v1/inventory.html"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    # Load page
    def load_page(self):
        self.driver.get(self.URL)


    # General util function to extract text
    def get_text(self,element):
        try:
            text = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, element))
            ).text
            return text
        except TimeoutException:
            return False
        
    # General util function to get single element
    def get_element(self,locator):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
            return element
        except TimeoutException:
            return False

            


        

    