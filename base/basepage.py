from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader

class BasePage:
    
# Research note: The timeout parameter in the __init__ method allows customization of the wait time for different pages or elements if needed.
# *locator is used to unpack the tuple when passing it to find_element method. I mean, if locator is (By.ID, "element_id"), then *locator unpacks it to By.ID, "element_id" when calling find_element.

    def __init__(self, driver):
        self.driver = driver
        config = ConfigReader()
        timeout = int(config.get('explicit_wait'))
        self.wait =  WebDriverWait(driver, timeout)
        
    def clickit(self, locator):
        # traditional / naive way of above
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        # element = self.driver.find_element(*locator)
        # element.click()
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        
    def typeit(self, locator, text):
        # traditional / naive way of above
        # element = self.driver.find_element(*locator)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        # element.send_keys(text)
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.driver.find_element(*locator).send_keys(text)
    
    def get_element_text(self, locator):
        # traditional / naive way of below line
        # driver = self.driver
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        # element = driver.find_element(*locator)
        # return element.text
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text
    
    def get_value_of_element(self, locator):
        # traditional / naive way of below line
        # driver = self.driver
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        # element = driver.find_element(*locator)
        # return element.get_attribute("value")
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).get_attribute("value")
    
    
    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except Exception:
            return False
        # traditional / naive way of below line
        # driver = self.driver
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        # element = driver.find_element(*locator)
        # return element.is_displayed()

    def accept_the_alert(self):
        alert = self.switch_to_alert()
        alert.accept()
        # Research note: No need to return anything here as accept() does not return any value.
    
    def navigate_to(self, url):
        self.driver.get(url)
    
    def get_page_title(self):
        return self.driver.title
    
    def switch_to_alert(self):
        return self.driver.switch_to.alert
    
    def get_element_attribute(self, locator, attribute_name):
        # Traditional / naive way of above lines
        # driver = self.driver <-- redundant
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator)) <-- redundant
        # element = driver.find_element(*locator) <-- redundant
        # return element.get_attribute(attribute_name)
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).get_attribute(attribute_name)
        
    def find_elements(self, locator):
        self.wait.until(lambda driver: len(driver.find_elements(*locator)) > 0)
        
    def pick_and_click_from_list(self, elements, text_to_select):
        for element in elements:
            if element.text == text_to_select:
                element.click()
                break