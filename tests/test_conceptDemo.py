# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager


import pytest
from flows.alert_flow import AlertFlow
from flows.autosuggestions_flow import AutoSuggestionsFlow
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
    alert_flow = AlertFlow(practice_page)
    alert_message = alert_flow.submit_name_and_get_alert_message(name_input)
    assert name_input in alert_message, "Alert message should contain the input name"

def test_autosuggestion_dropdown(practice_page):
    # Verify that user can type a partial country name, select a value from the auto-suggestion list, and the selected value is populated correctly.
    # Steps:
    # Type a partial country name into the autosuggestion input field.
    # Wait for the autosuggestion list to appear.
    # Select a country from the autosuggestion list.
    # Verify that the selected country is populated in the input field.
    autosuggestion_flow = AutoSuggestionsFlow(practice_page)
    partial_country_name = "Ind"
    full_country_name = "India"
    selected_country = autosuggestion_flow.select_country_from_autosuggestions(partial_country_name,full_country_name)
    assert selected_country == full_country_name, "Selected country should be populated correctly in the input field"

    
    
    

    
    
    
    