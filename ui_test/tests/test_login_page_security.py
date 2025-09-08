import pytest

from integration.db_connections.sql_connection.db_config import DBConfig
from integration.db_connections.sql_connection.sql_service import SQLService

from ui_test.pages.login_page import LoginPage
from ui_test.tests.base_test import BaseTest
import time


class TestLoginPage(BaseTest):
    @pytest.mark.parametrize(
        "get_browser",
        [
            {"browser": "chrome", "remote": False, "options": None, "url": "https://www.saucedemo.com/"}
        ],
        indirect=True
    )
    def test_login_authorized_user(self, get_browser):
        driver = get_browser
        db_config = DBConfig()
        sql_service = SQLService(db_config)
        login_page = LoginPage(driver)
        result = sql_service.select("select username , password from Users where username = 'standard_user'")

        user = result[0]["username"]
        password = (result[0]["password"])
        time.sleep(5)
        login_page.enter_username(user)
        login_page.enter_password(password)
        login_page.click_on_login_button()
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    @pytest.mark.parametrize(
        "get_browser",
        [
            {"browser": "chrome", "remote": True, "options": None, "url": "https://www.saucedemo.com/"}
        ],
        indirect=True
    )
    def test_login_unauthorized_user(self, get_browser):
        driver = get_browser
        login_page = LoginPage(driver)
        user = "vivi"
        password = "12345"
        login_page.enter_username(user)
        login_page.enter_password(password)
        time.sleep(5)
        login_page.click_on_login_button()
        assert driver.current_url == "https://www.saucedemo.com/"

    def test_for_parallel(self, get_browser):
        driver = get_browser
        login_page = LoginPage(driver)
        user = "vivi"
        password = "12345"
        login_page.enter_username(user)
        login_page.enter_password(password)
        time.sleep(5)
        login_page.click_on_login_button()
        assert driver.current_url == "https://www.saucedemo.com/"