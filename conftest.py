# tests/conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()

    if os.getenv("HEADLESS") == "1":
        # CI mode
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)  # fixed CI dimension
    else:
        # Local mode
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

    yield driver
    driver.quit()
