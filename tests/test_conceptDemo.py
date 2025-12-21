# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager


import pytest
from pages.practice_page import PracticePage

def test_initial(practice_page):
    assert "Practice Page" in practice_page.get_page_title()
    

def test_interacting_basic_web_elements_p1(practice_page):
    # Intracting clicks, input typing, element visiibility, title, submitting / button interactions
    # Scenario: Hide the text element and check if the element not visiible, then hit show and check if th eelement is visible. If it is viisble, then check if the element is typable

    practice_page.click_show_button()
    assert practice_page.is_textbox_displayed(), "Textbox should be visible after clicking show"

    practice_page.type_in_textbox("Haryish")
    assert practice_page.get_textbox_value() == "Haryish", "Typed value should be appeared"

    practice_page.click_hide_button()
    assert not practice_page.is_textbox_displayed(), "Textbox should be hidden after clicking hide"


def test_check_alert_message_content(practice_page):
    # 1. Trigger the alert.
    # 2. Check the message content of the alert.
    name_input = "Haryish ELangumaran"
    practice_page.trigger_alert_with_name_input(name_input)
    alert_message = practice_page.get_alert_text_and_accept()
    assert name_input in alert_message, "Alert message should contain the input name"



    
    
    

    
    
    
    