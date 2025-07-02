from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    CREATE_ACCOUNT = (By.CSS_SELECTOR, 'a[href*="create"]')
    LOGIN_LINK = (By.CSS_SELECTOR, 'a[href*="login"]')
    SWITCH_ACTION = (By.CSS_SELECTOR, ".panel.header .customer-welcome .action.switch")
    SIGNOUT_LINK = (By.LINK_TEXT, "Sign Out")

    def go_to_signup(self):
        self.click(self.CREATE_ACCOUNT)

    def go_to_login(self):
        self.click(self.LOGIN_LINK)

    def logout(self):
        self.click(self.SWITCH_ACTION)
        self.click(self.SIGNOUT_LINK)