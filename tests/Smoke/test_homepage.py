import allure
import pytest
from playwright.sync_api import Page, expect

from POM.base_page import BASE_URL, BasePage


@allure.title("Homepage loads")
@pytest.mark.smoke
def test_homepage_loads(page: Page):
    home = BasePage(page)
    home.open_homepage()

    expect(page).to_have_url(BASE_URL + "/")
    expect(page.locator("img.site-logo")).to_be_visible()
