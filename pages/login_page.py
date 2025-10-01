from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class LoginPage:
    URL = "https://www.saucedemo.com/v1/index.html"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    # Load page
    def load_page(self):
        self.driver.get(self.URL)

    # Login
    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

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

            


        

    