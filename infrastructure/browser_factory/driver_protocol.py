from typing import Protocol, Optional, List

from selenium.webdriver.remote.webdriver import WebDriver


class DriverProtocol(Protocol):
    def get_driver(self,browser_name: str, is_remote: bool, options: Optional[List[str]]) -> WebDriver:...