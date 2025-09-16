
import pytest

from infrastructure.browser_factory.browser_factory import *
class BaseTest:
    def open_page(self,url:str,driver:WebDriver)-> WebDriver:
        driver.get(url)
        driver.maximize_window()
        return driver

    @pytest.fixture
    def get_browser(self,request)-> WebDriver:
        driver_factory= DriverFactory()
        params = request.param
        browser_name = params["browser"]
        is_remote = params["remote"]
        options = params["options"]
        url = params["url"]
        driver=self.open_page(url,driver_factory.get_driver(browser_name, is_remote, options))
        yield driver
        driver.quit()


