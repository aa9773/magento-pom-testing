from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.ID, "send2")
    ERROR_MSG = (By.CSS_SELECTOR, ".message-error")

    def login(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_failed(self):
        return self.is_visible(self.ERROR_MSG)
