from POM.base_page import BASE_URL, BasePage
from POM.cart.cart_page import BONGOS_PATH

LOGIN_URL = BASE_URL + "/%d7%94%d7%a8%d7%a9%d7%9e%d7%aa%d7%9c%d7%a7%d7%95%d7%97"
MAP_URL = BASE_URL + "/%d7%9e%d7%a4%d7%aa-%d7%94%d7%92%d7%a2%d7%94-%d7%9e%d7%99%d7%95%d7%96%d7%99%d7%a7-%d7%92%d7%99%d7%99%d7%98"
GALLERY_URL = BASE_URL + "/%d7%92%d7%9c%d7%a8%d7%99%d7%99%d7%aa-%d7%aa%d7%9e%d7%95%d7%a0%d7%95%d7%aa"
TERMS_URL = BASE_URL + "/%d7%aa%d7%a7%d7%a0%d7%95%d7%9f-%d7%9e%d7%99%d7%95%d7%96%d7%99-%d7%92%d7%99%d7%99%d7%98"
INSTAGRAM_URL = "https://www.instagram.com/musicgate_israel/"


class FooterPage(BasePage):
    """Site footer - the same on every page."""

    def open_product_page(self):
        # Footer tests start from a product page, not the homepage
        self.open(BONGOS_PATH)

    def scroll_to_footer(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.page.evaluate("window.scrollTo(0, 0)")

    def footer(self):
        return self.page.locator(".site-footer")

    def footer_link(self, href: str):
        return self.footer().locator(f'a[href="{href}"]').first

    def logo(self):
        return self.page.locator("img.site-logo").first

    def login_link(self):
        return self.page.locator("a#menu-extra-login")

    def terms_link(self):
        return self.page.locator('a[rel="privacy-policy"]').first

    def instagram_link(self):
        return self.page.locator(f'a[href="{INSTAGRAM_URL}"]').first

    def facebook_link(self):
        return self.page.locator('a[href*="facebook.com"]').first

    def facebook_icon(self):
        return self.page.locator("i.fa.fa-facebook-f").first
