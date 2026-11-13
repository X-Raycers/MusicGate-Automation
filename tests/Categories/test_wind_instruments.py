import allure
import pytest
from playwright.sync_api import Page, expect

from POM.instruments.wind_instruments.wind_instruments_page import (
    SUBCATEGORIES,
    WIND_URL,
    WindInstrumentsPage,
)


@pytest.fixture
def wind_page(page: Page) -> WindInstrumentsPage:
    wind = WindInstrumentsPage(page)
    wind.open_homepage()
    return wind


@allure.title("Navigate to wind instruments main category")
def test_wind_main_category(wind_page: WindInstrumentsPage):
    wind_page.click_wind_main_category()

    expect(wind_page.page).to_have_url(WIND_URL)


@allure.title("Navigate to {subcategory} category")
@pytest.mark.parametrize("subcategory", list(SUBCATEGORIES))
def test_wind_subcategory(wind_page: WindInstrumentsPage, subcategory: str):
    wind_page.open_wind_menu()
    wind_page.click_subcategory(subcategory)

    _, expected_url = SUBCATEGORIES[subcategory]
    expect(wind_page.page).to_have_url(expected_url)
