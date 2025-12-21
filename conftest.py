import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.practice_page import PracticePage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    base_url = "https://rahulshettyacademy.com/AutomationPractice/"
    
    driver.get(base_url)
    
    yield driver
    
    driver.quit()
    

@pytest.fixture
def practice_page(driver):
    return PracticePage(driver)