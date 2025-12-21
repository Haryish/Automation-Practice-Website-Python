from selenium.webdriver.common.by import By
from base.basepage import BasePage

class PracticePage(BasePage):
    HIDE_BUTTON = (By.ID, "hide-textbox")
    SHOW_BUTTON = (By.ID, "show-textbox")
    TEXTBOX = (By.ID, "displayed-text")

    def click_hide_button(self):
        self.clickit(self.HIDE_BUTTON)

    def click_show_button(self):
        self.clickit(self.SHOW_BUTTON)

    def is_textbox_displayed(self):
        return self.is_element_displayed(self.TEXTBOX)
    
    def is_textbox_not_displayed(self):
        try:
            self.is_element_displayed(self.TEXTBOX)
            return True
        except Exception:
            return False

    def type_in_textbox(self, text):
        self.typeit(self.TEXTBOX, text)

    def get_textbox_value(self):
        return self.get_value_of_element(self.TEXTBOX)