from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class RemoteDriver:

    def __init__(self, executor_url='http://localhost:4444/wd/hub'):
        self.executor_url = executor_url

    def get_webdriver(self, browser_name: str):
        match browser_name.lower():
            case "chrome":
                return webdriver.Remote(
                    command_executor=self.executor_url,
                    options=ChromeOptions()
                )
            case "firefox":
                return webdriver.Remote(
                    command_executor=self.executor_url,
                    options=FirefoxOptions()
                )
            case _:
                raise ValueError(f"Unsupported browser: {browser_name}")

    def get_driver_with_options(self, browser_type: str, options_list: List[str]):
        match browser_type.lower():
            case "chrome":
                options = ChromeOptions()
                self.add_arguments_to_options(options, options_list)
                prefs = {"profile.default_content_setting_values.notifications": 2}
                options.add_experimental_option("prefs", prefs)
                return webdriver.Remote(
                    command_executor=self.executor_url,
                    options=options
                )

            case "firefox":
                options = FirefoxOptions()
                self.add_arguments_to_options(options, options_list)
                return webdriver.Remote(
                    command_executor=self.executor_url,
                    options=options
                )

            case _:
                raise ValueError(f"Unsupported browser type: {browser_type}")

    def add_arguments_to_options(self, options, arguments_list: List[str]):
        for argument in arguments_list:
            options.add_argument(f"--{argument}")
