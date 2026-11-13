from playwright.sync_api import expect

from POM.base_page import BASE_URL, BasePage

WIND_MENU_ITEM = "mega-menu-item-87506"
WIND_URL = f"{BASE_URL}/product-category/%d7%9b%d7%9c%d7%99-%d7%a0%d7%a9%d7%99%d7%a4%d7%94"

# name -> (menu item id, expected URL after click)
SUBCATEGORIES = {
    "harmonicas": ("mega-menu-item-87514", f"{WIND_URL}/%d7%9e%d7%a4%d7%95%d7%97%d7%99%d7%95%d7%aa"),
    "melodicas": ("mega-menu-item-87513", f"{WIND_URL}/%d7%9e%d7%9c%d7%95%d7%93%d7%99%d7%a7%d7%95%d7%aa"),
    "kazoo": ("mega-menu-item-87516", f"{WIND_URL}/%d7%a7%d7%90%d7%96%d7%95"),
}


class WindInstrumentsPage(BasePage):
    """Wind instruments section of the mega menu (opens on hover)."""

    def _wind_link(self):
        return self.page.locator(f"#{WIND_MENU_ITEM} > a.mega-menu-link")

    def open_wind_menu(self):
        link = self._wind_link()
        link.hover()
        expect(link).to_have_attribute("aria-expanded", "true")

    def click_wind_main_category(self):
        self.open_wind_menu()
        self._wind_link().click()

    def click_subcategory(self, name: str):
        item_id, _ = SUBCATEGORIES[name]
        self.page.locator(f"#{item_id} > a.mega-menu-link").click()
