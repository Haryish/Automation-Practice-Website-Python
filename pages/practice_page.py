from selenium.webdriver.common.by import By
from base.basepage import BasePage

class PracticePage(BasePage):
    HIDE_BUTTON = (By.ID, "hide-textbox")
    SHOW_BUTTON = (By.ID, "show-textbox")
    TEXTBOX = (By.ID, "displayed-text")
    ALERT_BUTTON = (By.ID, "alertbtn")
    NAME_INPUT = (By.ID, "name")    
    

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
    
    def get_alert_text_and_accept(self):
        alert = self.switch_to_alert()
        alert_text = alert.text
        alert.accept()
        return alert_text