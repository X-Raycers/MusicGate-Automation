import allure
import pytest
from playwright.sync_api import Page, expect

from POM.login.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.open_login_page()
    login.click_login_button()
    return login


@allure.title("Open login page")
@pytest.mark.smoke
def test_open_login_page(login_page: LoginPage):
    expect(login_page.login_text()).to_contain_text("התחברות")
    expect(login_page.username_field()).to_be_visible()


@allure.title("Login with empty fields")
def test_login_empty_fields(login_page: LoginPage):
    login_page.submit_login()

    expect(login_page.username_field()).to_be_visible()
    expect(login_page.password_field()).to_be_visible()


@allure.title("Invalid password login test")
def test_invalid_password(login_page: LoginPage):
    login_page.fill_password("wrongpassword")
    login_page.submit_login()

    expect(login_page.password_field()).to_be_visible()


@allure.title("Invalid email login test")
def test_invalid_email(login_page: LoginPage):
    login_page.fill_email("wrongemail@gmail.com")
    login_page.submit_login()

    expect(login_page.username_field()).to_be_visible()


@allure.title("Remember me checkbox test")
def test_remember_me_checkbox(login_page: LoginPage):
    login_page.click_remember_me_checkbox()

    expect(login_page.remember_me_checkbox()).to_be_checked()


@allure.title("Show password button test")
def test_show_password_button(login_page: LoginPage):
    login_page.fill_password("fakepassword123")
    login_page.click_show_password_button()

    expect(login_page.password_field()).to_have_attribute("type", "text")
