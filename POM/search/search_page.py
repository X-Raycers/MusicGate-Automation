from POM.base_page import BasePage


class SearchPage(BasePage):
    """Header product search and the search results page."""

    def search_box(self):
        return self.page.get_by_role("textbox")

    def search_with_button(self, text: str):
        self.search_box().fill(text)
        # The site has 2 search forms (normal + sticky header), use the first
        self.page.get_by_role("button", name="חפש").first.click()

    def search_with_enter(self, text: str):
        self.search_box().fill(text)
        self.page.keyboard.press("Enter")

    def click_sort_by_latest(self):
        # The sort options are a dropdown that opens on hover
        self.page.locator("ul.woocommerce-ordering li.current").hover()
        self.page.get_by_role("link", name="למיין לפי המעודכן ביותר").click()

    def catalog_title_h1(self):
        return self.page.locator("h1.mf-catalog-title")

    def catalog_title_h2(self):
        return self.page.locator("h2.mf-catalog-title")

    def body(self):
        return self.page.locator("body")
