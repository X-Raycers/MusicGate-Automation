import allure
import pytest
from playwright.sync_api import Page, expect

from POM.base_page import BASE_URL
from POM.footer.footer_page import (
    GALLERY_URL,
    INSTAGRAM_URL,
    LOGIN_URL,
    MAP_URL,
    TERMS_URL,
    FooterPage,
)


@pytest.fixture
def footer_page(page: Page) -> FooterPage:
    footer = FooterPage(page)
    footer.open_product_page()
    footer.scroll_to_footer()
    expect(footer.footer()).to_be_visible()
    return footer


@allure.title("Logo returns to homepage")
def test_logo_link(footer_page: FooterPage):
    footer_page.scroll_to_top()
    footer_page.logo().click()

    expect(footer_page.page).to_have_url(BASE_URL + "/")


@allure.title("Login link")
def test_login_link(footer_page: FooterPage):
    footer_page.login_link().click()

    expect(footer_page.page).to_have_url(LOGIN_URL)


@allure.title("Footer link: {name}")
@pytest.mark.parametrize(
    "name, url",
    [
        pytest.param("map", MAP_URL, id="map"),
        pytest.param("gallery", GALLERY_URL, id="gallery"),
    ],
)
def test_footer_links(footer_page: FooterPage, name: str, url: str):
    footer_page.footer_link(url).click()

    expect(footer_page.page).to_have_url(url)


@allure.title("Terms of use link")
def test_terms_link(footer_page: FooterPage):
    footer_page.terms_link().click()

    expect(footer_page.page).to_have_url(TERMS_URL)


@allure.title("Instagram opens in a new tab")
@pytest.mark.skip(reason="Instagram account no longer exists - link removed from site")
def test_instagram_link(footer_page: FooterPage):
    with footer_page.page.expect_popup() as popup_info:
        footer_page.instagram_link().click()
    instagram = popup_info.value

    expect(instagram).to_have_url(INSTAGRAM_URL)


@allure.title("Facebook link")
def test_facebook_link(footer_page: FooterPage):
    expect(footer_page.facebook_link()).to_be_visible()
    expect(footer_page.facebook_icon()).to_be_visible()
    expect(footer_page.facebook_link()).to_have_attribute("target", "_blank")
