import datetime
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import ConfigReader
from pages.practice_page import PracticePage
from utils.logger import get_logger

logger = get_logger()
logger.info("LOGGER SMOKE TEST")

def pytest_addoption(parser):
    # Add command line option to specify environment
    parser.addoption(
        "--env",
        action="store",
        default="default",
        help="Environment to run tests against (default/uat/prod)"
    )
    # Argument 1: --env - specifies the environment
    # Argument 2: action - store the value provided (means that the value will be stored)
    # Argument 2: default value - "default"
    # Argument 3: help - description of the argument

# Fixture to set up and tear down WebDriver
@pytest.fixture(scope="class")
def driver(request):  
    # Get the environment from command line option
    env = request.config.getoption("--env")
    # Set up WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    # Read base URL from config based on environment
    config = ConfigReader(env = env)
    base_url = config.get('base_url')
    
    # Navigate to the base URL
    driver.get(base_url)
    
    # Attach the driver to the request node for access in tests
    request.node.driver = driver
    assert hasattr(request.node, "driver"), "Driver not attached to request node"
    
    # Provide the driver to the tests
    yield driver
    
    # Quit the WebDriver after tests are done
    driver.quit()
    
@pytest.fixture(autouse=True)
def reset_page(driver):
    # Read base URL from config based on environment
    driver.refresh()
    

#BASIC IMPLEMENTATION OF LOGGING TEST RESULTS
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call":
#         if rep.passed:
#             logger.info(f"TEST PASSED: {item.name}")
#         elif rep.failed:
#             logger.error(f"TEST FAILED: {item.name}")
#         elif rep.skipped:
#             logger.warning(f"TEST SKIPPED: {item.name}")
#         elif rep.xfailed:
#             logger.warning(f"TEST XFAILED: {item.name}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        screenshots_dir = "screenshots"

    # if os.path.exists(screenshots_dir):
    #     screenshots = os.listdir(screenshots_dir)
    #     if screenshots:
    #         latest = max(
    #             [os.path.join(screenshots_dir, f) for f in screenshots],
    #             key=os.path.getctime
    #         )
    #         rep.extra = getattr(rep, "extra", [])
    #         rep.extra.append(pytest_html.extras.image(latest))

    # SKIPPED (happens in setup phase)
    if rep.when == "setup" and rep.skipped:
        logger.warning(f"TEST SKIPPED: {item.name}")

    # ACTUAL test execution
    if rep.when == "call":

        if rep.passed and hasattr(rep, "wasxfail"):
            logger.warning(f"TEST XPASSED (unexpected pass): {item.name}")

        elif rep.failed and hasattr(rep, "wasxfail"):
            logger.warning(f"TEST XFAILED (expected failure): {item.name}")

        elif rep.failed:
            logger.error(f"TEST FAILED: {item.name}")
            if driver:
                try:
                    screenshot_dir = "screenshots"
                    os.makedirs(screenshot_dir, exist_ok=True)
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")
                    item.driver.save_screenshot(screenshot_path)
                    logger.info(f"Screenshot saved to {screenshot_path}")
                except Exception as e:
                    logger.error(f"Failed to capture screenshot: {e}")
    
        elif rep.passed:
            logger.info(f"TEST PASSED: {item.name}")


# Fixture to provide PracticePage instance
@pytest.fixture
def practice_page(driver):
    return PracticePage(driver)