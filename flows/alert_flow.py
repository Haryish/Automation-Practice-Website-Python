#Intention: Define the AlertFlow class to manage alert-related workflows.
# This class can encapsulate methods to handle alerts, such as triggering alerts,
# retrieving alert messages, and accepting or dismissing alerts.
# Page class expose capabilities: 
# Flow class compose journeys
# Tests verify outcomes

class AlertFlow:
    def __init__(self, page):
        self.page = page
        
    def submit_name_and_get_alert_message(self,name):
        self.page.trigger_alert_with_name_input(name)
        alert_message = self.page.get_alert_text()
        print(alert_message)
        self.page.accept_the_alert()
        return alert_message