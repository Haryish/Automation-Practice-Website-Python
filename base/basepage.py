from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
# Research note: The timeout parameter in the __init__ method allows customization of the wait time for different pages or elements if needed.
# *locator is used to unpack the tuple when passing it to find_element method. I mean, if locator is (By.ID, "element_id"), then *locator unpacks it to By.ID, "element_id" when calling find_element.
# What I meant by "unpacked tuple" is that the locator parameter is expected to be a tuple containing two elements: the strategy to locate the element (like By.ID, By.NAME, etc.) and the actual value used for locating the element (like the specific ID or name). When we use *locator in the method calls, it unpacks this tuple into separate arguments for the find_element method.
# got it? yes madam.

    def __init__(self, driver, timeout = 10):
        self.driver = driver
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
    
    
    def is_element_displayed(self, locator):
        # traditional / naive way of below line
        # driver = self.driver
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        # element = driver.find_element(*locator)
        # return element.is_displayed()
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).is_displayed()
    
    
    def navigate_to(self, url):
        self.driver.get(url)
    
    def get_page_title(self):
        return self.driver.title
    
    def get_element_attribute(self, locator, attribute_name):
        # Traditional / naive way of above lines
        # driver = self.driver <-- redundant
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator)) <-- redundant
        # element = driver.find_element(*locator) <-- redundant
        # return element.get_attribute(attribute_name)
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).get_attribute(attribute_name)
        