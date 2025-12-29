from selenium.webdriver.common.by import By
from base.basepage import BasePage

class PracticePage(BasePage):
    HIDE_BUTTON = (By.ID, "hide-textbox")
    SHOW_BUTTON = (By.ID, "show-textbox")
    TEXTBOX = (By.ID, "displayed-text")
    ALERT_BUTTON = (By.ID, "alertbtn")
    NAME_INPUT = (By.ID, "name") 
    COUNTRY_INPUT = (By.ID, "autocomplete")
    SUGGESTIONS = (By.CSS_SELECTOR, ".ui-menu-item div")

    def click_hide_button(self):
        self.clickit(self.HIDE_BUTTON)

    def click_show_button(self):
        self.clickit(self.SHOW_BUTTON)

    def is_textbox_displayed(self):
        return self.is_visible(self.TEXTBOX)

    def type_in_textbox(self, text):
        self.typeit(self.TEXTBOX, text)

    def get_textbox_value(self):
        return self.get_value_of_element(self.TEXTBOX)
    
    def trigger_alert_with_name_input(self, name):
        self.typeit(self.NAME_INPUT, name)
        self.clickit(self.ALERT_BUTTON)
        
    def get_alert_text(self):
        alert = self.switch_to_alert()
        alert_text = alert.text
        return alert_text
    
    def enter_partial_country_name(self, partial_name):
        self.typeit(self.COUNTRY_INPUT, partial_name)
        
    def wait_for_autosuggestion_list(self):
        self.find_elements(self.SUGGESTIONS)
    
    def select_country_from_list(self, country_name):
        suggestions = self.driver.find_elements(*self.SUGGESTIONS)
        self.pick_and_click_from_list(suggestions, country_name)
    
    def get_selected_country(self):
        return self.get_value_of_element(self.COUNTRY_INPUT)
    
    def refresh_page(self):
        return super().refresh_page()
    

    