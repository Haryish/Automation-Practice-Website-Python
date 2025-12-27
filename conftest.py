import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import ConfigReader
from pages.practice_page import PracticePage

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="default",
        help="Environment to run tests against (default/uat/prod)"
    )



@pytest.fixture
def driver(request):
    env = request.config.getoption("--env")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    config = ConfigReader(env = env)
    base_url = config.get('base_url')
    
    driver.get(base_url)
    
    yield driver
    
    driver.quit()
    

@pytest.fixture
def practice_page(driver):
    return PracticePage(driver)