import re

import allure
import pytest
from playwright.sync_api import Page, expect

from POM.search.search_page import SearchPage

RESULTS_FOR = "תוצאות חיפוש עבור"


@pytest.fixture
def search_page(page: Page) -> SearchPage:
    search = SearchPage(page)
    search.open_homepage()
    return search


@allure.title("Open search")
def test_open_search(search_page: SearchPage):
    search_page.search_with_button("גיטרה")

    expect(search_page.body()).to_contain_text("גיטרה")


@allure.title("Search for '{text}'")
@pytest.mark.parametrize(
    "text",
    [
        pytest.param("CUENCA", id="existing_product", marks=pytest.mark.smoke),
        pytest.param("abcdefxyz123", id="invalid_product"),
        pytest.param("@#$%^&*!", id="special_characters"),
    ],
)
def test_search_shows_results_page(search_page: SearchPage, text: str):
    search_page.search_with_enter(text)

    expect(search_page.page).to_have_url(re.compile(r"[?&]s="))
    expect(search_page.catalog_title_h2()).to_contain_text(text)


@allure.title("Search results title is in Hebrew")
@pytest.mark.xfail(
    reason="BUG: on the Hebrew site the results title is shown in English "
    "('Search Results for ...' instead of 'תוצאות חיפוש עבור ...')"
)
def test_search_results_title_in_hebrew(search_page: SearchPage):
    search_page.search_with_enter("גיטרה")

    expect(search_page.catalog_title_h2()).to_contain_text(RESULTS_FOR)


@allure.title("Empty search")
def test_empty_search(search_page: SearchPage):
    search_page.search_with_enter("")

    expect(search_page.catalog_title_h1()).to_contain_text("תוצאות חיפוש")


@allure.title("Sort search results by latest")
def test_navigate_from_search(search_page: SearchPage):
    search_page.search_with_enter("גיטרה")
    search_page.click_sort_by_latest()

    expect(search_page.page).to_have_url(re.compile(r"orderby=date"))
    expect(search_page.body()).to_contain_text("גיטרה")
