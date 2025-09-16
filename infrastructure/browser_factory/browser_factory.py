from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver

from infrastructure.browser_factory.driver_protocol import DriverProtocol
from infrastructure.browser_factory.local_driver import *
from infrastructure.browser_factory.remote_driver import RemoteDriver


class DriverFactory(DriverProtocol):

    def get_driver(self,browser_name: str, is_remote: bool, options: Optional[List[str]])-> WebDriver:  # type: ignore
        if is_remote:
            return self.get_remote_driver(browser_name, options)
        return self.get_local_driver(browser_name,options)



    def get_local_driver(self,browser_name: str,options: Optional[List[str]])-> WebDriver:
        local_driver = LocalDriver()
        if options is None:
            return local_driver.get_webdriver(browser_name)
        return local_driver.get_driver_with_options(browser_name,options)

    def get_remote_driver(self,browser_name: str,options: Optional[List[str]])-> WebDriver:
        remote_driver = RemoteDriver()
        if options is None:
            return remote_driver.get_webdriver(browser_name)
        return remote_driver.get_driver_with_options(browser_name, options)
