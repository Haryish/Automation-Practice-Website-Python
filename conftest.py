import datetime
import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import ConfigReader
from pages.practice_page import PracticePage
from utils.logger import get_logger

logger = get_logger()           # 🔧 UPDATED: logger instance
ACTIVE_DRIVER = None            # 🔧 UPDATED: global driver reference

# Add command line option to specify environment
def pytest_addoption(parser):
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
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run tests in headless mode"
    )

# Fixture to initialize and provide WebDriver instance
@pytest.fixture(scope="class")
def driver(request):
    #🔧 UPDATED: global driver reference
    global ACTIVE_DRIVER    

    # Get environment from command line option
    env = request.config.getoption("--env")  
    headless = request.config.getoption("--headless")

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    
    if headless:
        options.add_argument("--headless-new")
        options.add_argument("--window-size=1920,1080")        
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    # Read base URL from config based on environment
    config = ConfigReader(env=env)
    base_url = config.get("base_url")
    driver.get(base_url)

    # attach driver for hooks
    request.node.driver = driver
    ACTIVE_DRIVER = driver

    # ❌ DO NOT quit here
    yield driver
    
@pytest.fixture(autouse=True)
def refresh_page(driver):
    # Read base URL from config based on environment
    driver.refresh()
    
# UPDATED: session-level teardown
@pytest.fixture(scope="session", autouse=True)
def quit_browser_session():
    yield
    global ACTIVE_DRIVER
    if ACTIVE_DRIVER:
        try:
            ACTIVE_DRIVER.quit()
            logger.info("Browser quit at session end")
        except Exception as e:
            logger.warning(f"Failed to quit browser at session end: {e}")

# Helper Functions for Test Reporting and Screenshots
def log_test_outcome(rep, item):
    if rep.passed and hasattr(rep, "wasxfail"):
        logger.warning(f"TEST XPASSED: {item.name} (was marked xfail but passed)")
    elif rep.failed and hasattr(rep, "wasxfail"):
        logger.warning(f"TEST XFAILED (expected failure): {item.name}")
    elif rep.failed:
        logger.error(f"TEST FAILED: {item.name}")
    elif rep.passed:
        logger.info(f"TEST PASSED: {item.name}")

def capture_screenshot(item):
    try:
        global ACTIVE_DRIVER
        driver = ACTIVE_DRIVER
        if not driver:
            logger.warning("Driver not available for screenshot")
            return

        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        # Generate timestamped screenshot filename for HTML report
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(
            screenshot_dir, f"{item.name}_{timestamp}.png"
        )
        driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved to {screenshot_path}")
        
        # Attach screenshot to Allure report
        png = driver.get_screenshot_as_png()
        allure.attach(
            png,
            name=f"{item.name}_failure",
            attachment_type=allure.attachment_type.PNG
        )
        logger.info("Screenshot attached to Allure report")

    except Exception as e:
        logger.error(f"Failed to capture screenshot: {e}")

def log_skipped_test(rep, item):
    if rep.when == "setup" and rep.skipped:
        logger.warning(f"TEST SKIPPED: {item.name}")

# Pytest hook to log test results and capture screenshots on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    log_skipped_test(rep, item)  # Log skipped tests (Helper Function)

    if rep.when == "call":
        log_test_outcome(rep, item)  # Log test outcome (Helper Function)

        if rep.failed and not hasattr(rep, "wasxfail"):
            capture_screenshot(item)  # Capture screenshot on failure (Helper Function)


# Fixture to provide PracticePage instance
@pytest.fixture
def practice_page(driver):
    return PracticePage(driver)



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