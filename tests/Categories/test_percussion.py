import allure
import pytest
from playwright.sync_api import Page, expect

from POM.instruments.percussion.percussion_page import (
    PERCUSSION_URL,
    SUBCATEGORIES,
    PercussionPage,
)


@pytest.fixture
def percussion_page(page: Page) -> PercussionPage:
    percussion = PercussionPage(page)
    percussion.open_homepage()
    return percussion


@allure.title("Navigate to percussion main category")
def test_percussion_main_category(percussion_page: PercussionPage):
    percussion_page.click_percussion_main_category()

    expect(percussion_page.page).to_have_url(PERCUSSION_URL)


@allure.title("Navigate to {subcategory} category")
@pytest.mark.parametrize("subcategory", list(SUBCATEGORIES))
def test_percussion_subcategory(percussion_page: PercussionPage, subcategory: str):
    percussion_page.open_percussion_menu()
    percussion_page.click_subcategory(subcategory)

    _, expected_url = SUBCATEGORIES[subcategory]
    expect(percussion_page.page).to_have_url(expected_url)
