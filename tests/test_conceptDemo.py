# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager


import pytest
from flows.alert_flow import AlertFlow
from flows.autosuggestions_flow import AutoSuggestionsFlow
from pages.practice_page import PracticePage
from utils.logger import get_logger
from utils.datareader import load_testdata as testdata
from utils.datareader import load_csvtestdata as csvdata

datajson = testdata("./data/autosuggestion_entries.json")
datacsv = csvdata("./data/autosuggestion_entries.csv")
logger = get_logger()

class TestConcept:
    def test_initial(self, practice_page):
        logger.info("Starting test_initial")
        # Verify that the Practice Page loads successfully by checking the page title
        assert "Practice Page" in practice_page.get_page_title()
        
    @pytest.mark.xfail(reason="Demonstration of pytest xfail functionality")
    def test_interacting_textbox_and_buttons(self, practice_page):
        # Intracting clicks, input typing, element visiibility, title, submitting / button interactions
        # Scenario: Hide the text element and check if the element not visiible, then hit show and check if th eelement is visible. If it is viisble, then check if the element is typable

        practice_page.click_show_button()
        assert practice_page.is_textbox_displayed(), "Textbox should be visible after clicking show"

        practice_page.type_in_textbox("Haryish")
        assert practice_page.get_textbox_value() == "Haryish", "Typed value should be appeared"

        practice_page.click_hide_button()
        assert not practice_page.is_textbox_displayed(), "Textbox should be hidden after clicking hide"

    @pytest.mark.skip(reason="Demonstration of pytest skip functionality")
    def test_check_alert_message_content(self, practice_page):
        # 1. Trigger the alert.
        # 2. Check the message content of the alert.
        name_input = "Haryish ELangumaran"
        alert_flow = AlertFlow(practice_page)
        alert_message = alert_flow.submit_name_and_get_alert_message(name_input)
        assert name_input in alert_message, "Alert message should contain the input name"

    def test_autosuggestion_dropdown_naive(self, practice_page):
        # Verify that user can type a partial country name, select a value from the auto-suggestion list, and the selected value is populated correctly.
        # Steps:
        # Type a partial country name into the autosuggestion input field.
        # Wait for the autosuggestion list to appear.
        # Select a country from the autosuggestion list.
        # Verify that the selected country is populated in the input field.
        autosuggestion_flow = AutoSuggestionsFlow(practice_page)
        selected_country = autosuggestion_flow.select_country_from_autosuggestions("Ind", "India")
        assert selected_country == "India", "Selected country should be populated correctly in the input field"

    @pytest.mark.parametrize("partial_country_name, full_country_name", [
        ("Ind", "India"),
        ("Uni", "United States of America"),
        ("Aus", "Australia")
        ]
    )
    def test_autosuggestion_dropdown_method1(self, practice_page, partial_country_name, full_country_name):
        # This is similar to above but we use parametrize to run the same test with multiple data sets
        # Verify that user can type a partial country name, select a value from the auto-suggestion list, and the selected value is populated correctly.
        autosuggestion_flow = AutoSuggestionsFlow(practice_page)
        selected_country = autosuggestion_flow.select_country_from_autosuggestions(partial_country_name, full_country_name)
        assert selected_country == full_country_name, "Selected country should be populated correctly in the input field"

    @pytest.mark.parametrize("dataset", datajson)
    def test_autosuggestion_dropdown_method2(self, practice_page, dataset):
        # This is method 2 of data driven testing using external json file
        # Verify that user can type a partial country name, select a value from the auto-suggestion list, and the selected value is populated correctly.
        autosuggestion_flow = AutoSuggestionsFlow(practice_page)
        selected_country = autosuggestion_flow.select_country_from_autosuggestions(dataset["partial_name"], dataset["full_name"])
        assert selected_country == dataset["full_name"], "Selected country should be populated correctly in the input field"

    @pytest.mark.parametrize("datacsv", datacsv)
    def test_autosuggestion_dropdown_method3(self, practice_page, datacsv):
        # This is method 3 of data driven testing using fixture to read external csv file
        # Verify that user can type a partial country name, select a value from the auto-suggestion list, and the selected value is populated correctly.
        practice_page.refresh_page()
        autosuggestion_flow = AutoSuggestionsFlow(practice_page)
        selected_country = autosuggestion_flow.select_country_from_autosuggestions(datacsv["partial_name"], datacsv["full_country_name"])
        assert selected_country == datacsv["full_country_name"], "Selected country should be populated correctly in the input field"