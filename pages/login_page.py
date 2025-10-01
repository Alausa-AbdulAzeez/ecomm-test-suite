from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
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



            


        

    