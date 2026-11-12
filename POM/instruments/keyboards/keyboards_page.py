from playwright.sync_api import expect

from POM.base_page import BASE_URL, BasePage

KEYBOARDS_MENU_ITEM = "mega-menu-item-87457"
KEYBOARDS_URL = f"{BASE_URL}/product-category/%d7%90%d7%95%d7%a8%d7%92%d7%a0%d7%99%d7%95%d7%aa-%d7%95%d7%a4%d7%a1%d7%a0%d7%aa%d7%a8%d7%99%d7%9d"

# name -> (menu item id, expected URL after click)
SUBCATEGORIES = {
    "keyboards": (
        "mega-menu-item-87458",
        f"{KEYBOARDS_URL}/%d7%90%d7%95%d7%a8%d7%92%d7%a0%d7%99%d7%95%d7%aa",
    ),
    "electric_pianos": (
        "mega-menu-item-87462",
        f"{KEYBOARDS_URL}/%d7%a4%d7%a1%d7%a0%d7%aa%d7%a8-%d7%97%d7%a9%d7%9e%d7%9c%d7%99",
    ),
    # Listed under the keyboards menu, but the page lives under guitar accessories
    "sheet_music_stands": (
        "mega-menu-item-87468",
        f"{BASE_URL}/product-category/%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d-%d7%9c%d7%92%d7%99%d7%98%d7%a8%d7%94/%d7%a2%d7%9e%d7%95%d7%93%d7%99-%d7%aa%d7%95%d7%99%d7%9d",
    ),
}


class KeyboardsPage(BasePage):
    """Keyboards & pianos section of the mega menu (opens on hover)."""

    def _keyboards_link(self):
        return self.page.locator(f"#{KEYBOARDS_MENU_ITEM} > a.mega-menu-link")

    def open_keyboards_menu(self):
        link = self._keyboards_link()
        link.hover()
        expect(link).to_have_attribute("aria-expanded", "true")

    def click_keyboards_main_category(self):
        self.open_keyboards_menu()
        self._keyboards_link().click()

    def click_subcategory(self, name: str):
        item_id, _ = SUBCATEGORIES[name]
        self.page.locator(f"#{item_id} > a.mega-menu-link").click()
