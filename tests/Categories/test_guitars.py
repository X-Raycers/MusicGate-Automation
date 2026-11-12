import re

import allure
import pytest
from playwright.sync_api import Page, expect

from POM.instruments.guitars.guitars_page import (
    GUITARS_URL,
    SUBCATEGORY_URLS,
    GuitarsPage,
)


@pytest.fixture
def guitars_page(page: Page) -> GuitarsPage:
    guitars = GuitarsPage(page)
    guitars.open_homepage()
    return guitars


@allure.title("Verify guitars category page title")
def test_guitars_main_category(guitars_page: GuitarsPage):
    guitars_page.click_guitars_main_category()

    expect(guitars_page.page).to_have_url(GUITARS_URL)
    expect(guitars_page.page).to_have_title(re.compile("גיטרות"))


@allure.title("Navigate to {subcategory} guitars category")
@pytest.mark.parametrize("subcategory", ["acoustic", "electric", "classical"])
def test_guitars_subcategory(guitars_page: GuitarsPage, subcategory: str):
    guitars_page.open_guitars_menu()
    guitars_page.click_subcategory(subcategory)

    expect(guitars_page.page).to_have_url(SUBCATEGORY_URLS[subcategory])
