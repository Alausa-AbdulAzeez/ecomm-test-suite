import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Setup (before test)
    driver = webdriver.Chrome()  
    driver.maximize_window()
    yield driver
    # Teardown (after test)
    driver.quit()
