from playwright.sync_api import expect

from POM.base_page import BASE_URL, BasePage

PERCUSSION_MENU_ITEM = "mega-menu-item-87484"
PERCUSSION_URL = f"{BASE_URL}/product-category/%d7%aa%d7%95%d7%a4%d7%99%d7%9d-%d7%95%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94"

# name -> (menu item id, expected URL after click)
SUBCATEGORIES = {
    "darbukas": ("mega-menu-item-87488", f"{PERCUSSION_URL}/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94-%d7%93%d7%a8%d7%91%d7%95%d7%a7%d7%94"),
    "bongos": ("mega-menu-item-88211", f"{PERCUSSION_URL}/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1"),
    "xylophones": ("mega-menu-item-88216", f"{PERCUSSION_URL}/%d7%a7%d7%a1%d7%99%d7%9c%d7%95%d7%a4%d7%95%d7%a0%d7%99%d7%9d"),
}


class PercussionPage(BasePage):
    """Percussion section of the mega menu (opens on hover)."""

    def _percussion_link(self):
        return self.page.locator(f"#{PERCUSSION_MENU_ITEM} > a.mega-menu-link")

    def open_percussion_menu(self):
        link = self._percussion_link()
        link.hover()
        expect(link).to_have_attribute("aria-expanded", "true")

    def click_percussion_main_category(self):
        self.open_percussion_menu()
        self._percussion_link().click()

    def click_subcategory(self, name: str):
        item_id, _ = SUBCATEGORIES[name]
        self.page.locator(f"#{item_id} > a.mega-menu-link").click()
