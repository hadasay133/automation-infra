from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from ui_test.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def enter_username(self,username):
        username_input = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
        self.sendkeys_into_element(username_input,username)

    def enter_password(self, password):
        password_input = self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Password']")
        self.sendkeys_into_element(password_input, password)
    def click_on_login_button(self):
        login_button = self.driver.find_element(By.ID, "login-button")
        self.click_on_button(login_button)