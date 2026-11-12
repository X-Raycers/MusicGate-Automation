import allure
import pytest
from playwright.sync_api import Page, expect

from POM.instruments.amplifiers.amplifiers_page import (
    AMPLIFIERS_URL,
    SUBCATEGORIES,
    AmplifiersPage,
)


@pytest.fixture
def amplifiers_page(page: Page) -> AmplifiersPage:
    amplifiers = AmplifiersPage(page)
    amplifiers.open_homepage()
    return amplifiers


@allure.title("Navigate to amplifiers main category")
def test_amplifiers_main_category(amplifiers_page: AmplifiersPage):
    amplifiers_page.click_amplifiers_main_category()

    expect(amplifiers_page.page).to_have_url(AMPLIFIERS_URL)


@allure.title("Navigate to {subcategory} category")
@pytest.mark.parametrize("subcategory", list(SUBCATEGORIES))
def test_amplifiers_subcategory(amplifiers_page: AmplifiersPage, subcategory: str):
    amplifiers_page.open_amplifiers_menu()
    amplifiers_page.click_subcategory(subcategory)

    _, expected_url = SUBCATEGORIES[subcategory]
    expect(amplifiers_page.page).to_have_url(expected_url)
