import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage

def test_magento_flows():
    fake = Faker()
    user = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.ascii_email(),
        "password": "TestPassword123!"
    }

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    base_url = "https://magento.softwaretestingboard.com/"

    try:
        driver.get(base_url)

        home = HomePage(driver)
        signup = SignupPage(driver)
        login = LoginPage(driver)
        reset = ResetPasswordPage(driver)

        # SIGNUP
        print("📝 Signup Flow")
        home.go_to_signup()
        signup.create_account(user)
        assert signup.is_account_created()
        print("✅ Signup Successful")

        # LOGOUT & LOGIN
        print("🔓 Logout & Login Flow")
        home.logout()
        home.go_to_login()
        login.login(user["email"], user["password"])
        assert signup.is_account_created()
        print("✅ Login Successful")

        # PASSWORD RESET
        print("🔑 Password Reset Flow")
        home.logout()
        home.go_to_login()
        reset.reset_password(user["email"])
        assert reset.is_reset_successful()
        print("✅ Password reset initiated")

        # INVALID LOGIN
        print("🚫 Invalid Login Flow")
        driver.get(f"{base_url}/customer/account/login/")
        login.login("wrong@test.com", "wrongpass")
        assert login.is_login_failed()
        print("✅ Invalid login correctly handled")

    finally:
        time.sleep(2)
        driver.quit()
