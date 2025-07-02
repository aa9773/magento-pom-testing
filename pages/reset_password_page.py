from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ResetPasswordPage(BasePage):
    FORGOT_LINK = (By.CSS_SELECTOR, "a.action.remind")
    EMAIL_INPUT = (By.ID, "email_address")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.action.submit.primary")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".message-success")

    def reset_password(self, email):
        self.click(self.FORGOT_LINK)
        self.enter_text(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BUTTON)

    def is_reset_successful(self):
        return self.is_visible(self.SUCCESS_MSG)
