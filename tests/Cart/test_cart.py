import allure
import pytest
from playwright.sync_api import Page, expect

from POM.cart.cart_page import (
    BONGOS_PRODUCT_ID,
    BONGOS_TITLE,
    GUITAR_PRODUCT_ID,
    GUITAR_TITLE,
    CartPage,
)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def cart_with_bongos(cart_page: CartPage) -> CartPage:
    """Adds the bongos to the cart and opens the cart page."""
    cart_page.open_bongos_product_page()
    expect(cart_page.product_title()).to_contain_text(BONGOS_TITLE)
    cart_page.add_to_cart(BONGOS_PRODUCT_ID)
    cart_page.open_cart()
    return cart_page


@allure.title("Add product to cart")
@pytest.mark.smoke
def test_add_product_to_cart(cart_with_bongos: CartPage):
    expect(cart_with_bongos.cart_items()).to_have_count(1)


@allure.title("Remove product from cart")
def test_remove_product_from_cart(cart_with_bongos: CartPage):
    cart_with_bongos.remove_product_from_cart()

    expect(cart_with_bongos.cart_items()).to_have_count(0)


@allure.title("Increase product quantity")
def test_increase_product_quantity(cart_with_bongos: CartPage):
    cart_with_bongos.increase_quantity()

    expect(cart_with_bongos.quantity_input()).to_have_value("2")


@allure.title("Decrease product quantity")
def test_decrease_product_quantity(cart_with_bongos: CartPage):
    cart_with_bongos.increase_quantity()
    expect(cart_with_bongos.quantity_input()).to_have_value("2")

    cart_with_bongos.decrease_quantity()

    expect(cart_with_bongos.quantity_input()).to_have_value("1")


@allure.title("Multiple products in cart")
def test_multiple_products_in_cart(cart_page: CartPage):
    cart_page.open_bongos_product_page()
    expect(cart_page.product_title()).to_contain_text(BONGOS_TITLE)
    cart_page.add_to_cart(BONGOS_PRODUCT_ID)

    cart_page.open_guitar_product_page()
    expect(cart_page.product_title()).to_contain_text(GUITAR_TITLE)
    cart_page.add_to_cart(GUITAR_PRODUCT_ID)

    cart_page.open_cart()

    expect(cart_page.cart_counter()).to_have_text("2")
