import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()