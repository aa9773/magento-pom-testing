from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):
    FIRSTNAME = (By.ID, "firstname")
    LASTNAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    CREATE_BUTTON = (By.CSS_SELECTOR, 'button[title="Create an Account"]')
    WELCOME_TEXT = (By.CSS_SELECTOR, ".page-title")
    GREET_TEXT = (By.CSS_SELECTOR, ".panel.header li.greet.welcome")

    def create_account(self, user):
        self.enter_text(self.FIRSTNAME, user["first_name"])
        self.enter_text(self.LASTNAME, user["last_name"])
        self.enter_text(self.EMAIL, user["email"])
        self.enter_text(self.PASSWORD, user["password"])
        self.enter_text(self.CONFIRM_PASSWORD, user["password"])
        self.click(self.CREATE_BUTTON)

    def is_account_created(self):
        return "Welcome" in self.get_text(self.GREET_TEXT)
