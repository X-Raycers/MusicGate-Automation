from POM.base_page import BasePage

# The old FLEET bongos product was removed from the site (404), so we use SONOR bongos
BONGOS_PATH = "/product/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1-sonor-7-8-bongo-natural-high-gloss-hevea-wood"
BONGOS_TITLE = "בונגוס SONOR"
BONGOS_PRODUCT_ID = "75009"

# The red CORT X-200 is out of stock (no add-to-cart button), so we use the black one
GUITAR_PATH = "/product/%d7%92%d7%99%d7%98%d7%a8%d7%94-%d7%97%d7%a9%d7%9e%d7%9c%d7%99%d7%aa-%d7%91%d7%a6%d7%91%d7%a2-%d7%a9%d7%97%d7%95%d7%a8-cort-x-200-bk-hsh"
GUITAR_TITLE = "CORT X-200 BK HSH"
GUITAR_PRODUCT_ID = "94498"

CART_PATH = "/cart"


class CartPage(BasePage):
    """Product pages and the shopping cart."""

    # ----- product page -----
    def open_bongos_product_page(self):
        self.open(BONGOS_PATH)

    def open_guitar_product_page(self):
        self.open(GUITAR_PATH)

    def product_title(self):
        return self.page.locator("h1.product_title.entry-title")

    def add_to_cart(self, product_id: str):
        # When you click "add to cart", the site sends a POST request
        # to the product page in the background (AJAX).
        # We wait for the server's answer to that request, so we know
        # the product was really saved in the cart before we move on.
        with self.page.expect_response(
            lambda r: r.request.method == "POST" and "/product/" in r.url
        ):
            self.page.locator(
                f'form.cart button[name="add-to-cart"][value="{product_id}"]'
            ).click()

    # ----- cart page -----
    def open_cart(self):
        self.open(CART_PATH)

    def cart_items(self):
        return self.page.locator("td.product-remove a")

    def remove_product_from_cart(self):
        self.page.locator('td.product-remove a[href*="remove_item"]').first.click()

    def increase_quantity(self):
        self.page.locator("div.qty-box span.increase.icon_plus").first.click()

    def decrease_quantity(self):
        self.page.locator("div.qty-box span.decrease.icon_minus-06").first.click()

    def quantity_input(self):
        return self.page.locator("input.input-text.qty.text").first

    def cart_counter(self):
        return self.page.locator(
            "a#icon-cart-contents span.mini-item-counter.mf-background-primary"
        )
