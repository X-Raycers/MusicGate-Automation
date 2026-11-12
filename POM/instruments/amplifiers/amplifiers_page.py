from playwright.sync_api import expect

from POM.base_page import BASE_URL, BasePage

AMPLIFIERS_URL = f"{BASE_URL}/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d"

# name -> (menu item id, expected URL after click)
SUBCATEGORIES = {
    "electric_guitar_amps": (
        "mega-menu-item-87454",
        f"{AMPLIFIERS_URL}/shoes",
    ),
    "acoustic_guitar_amps": (
        "mega-menu-item-87452",
        f"{AMPLIFIERS_URL}/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d-%d7%9c%d7%92%d7%99%d7%98%d7%a8%d7%94-%d7%90%d7%a7%d7%95%d7%a1%d7%98%d7%99%d7%aa",
    ),
    "accessories": (
        "mega-menu-item-87451",
        f"{AMPLIFIERS_URL}/%D7%90%D7%91%D7%99%D7%96%D7%A8%D7%99%D7%9D-%D7%9C%D7%9E%D7%92%D7%91%D7%A8%D7%99%D7%9D",
    ),
}


class AmplifiersPage(BasePage):
    """Amplifiers section of the mega menu (opens on hover)."""

    def _amplifiers_link(self):
        return self.page.locator(f'a.mega-menu-link[href="{AMPLIFIERS_URL}"]')

    def open_amplifiers_menu(self):
        link = self._amplifiers_link()
        link.hover()
        expect(link).to_have_attribute("aria-expanded", "true")

    def click_amplifiers_main_category(self):
        self.open_amplifiers_menu()
        self._amplifiers_link().click()

    def click_subcategory(self, name: str):
        item_id, _ = SUBCATEGORIES[name]
        self.page.locator(f"#{item_id} > a.mega-menu-link").click()
