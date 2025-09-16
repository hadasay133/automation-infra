from telnetlib import EC
from selenium.webdriver.support import expected_conditions as  EC


from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver:WebDriver) -> None:
        self.driver = driver

    def check_element_if_visible(self,element:WebElement):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of(element)
        )
        return element.is_displayed()

    def sendkeys_into_element(self,element:WebElement,value):
        element.send_keys(value)

    def click_on_button(self,element:WebElement):
        self.check_element_if_visible(element)
        element.click()