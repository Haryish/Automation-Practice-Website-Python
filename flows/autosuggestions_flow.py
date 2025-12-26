class AutoSuggestionsFlow:
    def __init__(self, practice_page):
        self.practice_page = practice_page

    def select_country_from_autosuggestions(self, partial_country_name, full_country_name):
        # Type the partial country name into the autosuggestion input field
        self.practice_page.enter_partial_country_name(partial_country_name)
        
        # Wait for the autosuggestion list to appear
        self.practice_page.wait_for_autosuggestion_list()
        
        # Select the desired country from the autosuggestion list
        self.practice_page.select_country_from_list(full_country_name)
        
        # Verify that the selected country is populated in the input field
        selected_country = self.practice_page.get_selected_country()
        return selected_country