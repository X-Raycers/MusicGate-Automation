import allure
import pytest
from playwright.sync_api import Page, expect

from POM.instruments.keyboards.keyboards_page import (
    KEYBOARDS_URL,
    SUBCATEGORIES,
    KeyboardsPage,
)


@pytest.fixture
def keyboards_page(page: Page) -> KeyboardsPage:
    keyboards = KeyboardsPage(page)
    keyboards.open_homepage()
    return keyboards


@allure.title("Navigate to keyboards main category")
def test_keyboards_main_category(keyboards_page: KeyboardsPage):
    keyboards_page.click_keyboards_main_category()

    expect(keyboards_page.page).to_have_url(KEYBOARDS_URL)


@allure.title("Navigate to {subcategory} category")
@pytest.mark.parametrize("subcategory", list(SUBCATEGORIES))
def test_keyboards_subcategory(keyboards_page: KeyboardsPage, subcategory: str):
    keyboards_page.open_keyboards_menu()
    keyboards_page.click_subcategory(subcategory)

    _, expected_url = SUBCATEGORIES[subcategory]
    expect(keyboards_page.page).to_have_url(expected_url)
