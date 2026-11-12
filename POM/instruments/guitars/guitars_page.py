from playwright.sync_api import expect

from POM.base_page import BASE_URL, BasePage

# Category paths (URL-encoded Hebrew slugs from the site)
GUITARS_PATH = "/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa"
ACOUSTIC_PATH = f"{GUITARS_PATH}/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%90%d7%a7%d7%95%d7%a1%d7%98%d7%99%d7%95%d7%aa"
ELECTRIC_PATH = f"{GUITARS_PATH}/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%97%d7%a9%d7%9e%d7%9c%d7%99%d7%95%d7%aa"
CLASSICAL_PATH = f"{GUITARS_PATH}/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%a7%d7%9c%d7%90%d7%a1%d7%99%d7%95%d7%aa"

GUITARS_URL = f"{BASE_URL}{GUITARS_PATH}"
SUBCATEGORY_URLS = {
    "acoustic": f"{BASE_URL}{ACOUSTIC_PATH}",
    "electric": f"{BASE_URL}{ELECTRIC_PATH}",
    "classical": f"{BASE_URL}{CLASSICAL_PATH}",
}


class GuitarsPage(BasePage):
    """Guitars section of the mega menu (Max Mega Menu, hover_intent)."""

    def _menu_link(self, url: str):
        return self.page.locator(f'a.mega-menu-link[href="{url}"]')

    def open_guitars_menu(self):
        # The menu opens on hover; a click before it is open only opens it
        guitars = self._menu_link(GUITARS_URL)
        guitars.hover()
        expect(guitars).to_have_attribute("aria-expanded", "true")

    def click_guitars_main_category(self):
        # "second click = go": open the menu first, then the click navigates
        self.open_guitars_menu()
        self._menu_link(GUITARS_URL).click()

    def click_subcategory(self, name: str):
        """name: 'acoustic', 'electric' or 'classical'."""
        self._menu_link(SUBCATEGORY_URLS[name]).click()
