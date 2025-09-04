from typing import List

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class LocalDriver:


    def get_webdriver(self,browser_name):
        match browser_name.lower():
            case 'firefox':
                return webdriver.Firefox()
            case 'chrome':
                return webdriver.Chrome()
            case 'ie':
                return webdriver.Ie()
            case _:
                raise ValueError(f"Browser '{browser_name}' is not supported.")


    def get_driver_with_options(self,browser_type: str, options_list: List[str]):
        match browser_type.lower():
            case "chrome":
                options = ChromeOptions()
                self.add_arguments_to_options(options, options_list)
                prefs = {"profile.default_content_setting_values.notifications": 2}
                options.add_experimental_option("prefs", prefs)
                return webdriver.Chrome(options=options)

            case "firefox":
                options = FirefoxOptions()
                self.add_arguments_to_options(options, options_list)
                return webdriver.Firefox(options=options)

            case _:
                raise ValueError(f"Unsupported browser type: {browser_type}")

    def add_arguments_to_options(self,options, arguments_list: List[str]):
        for argument in arguments_list:
            options.add_argument(f"--{argument}")
