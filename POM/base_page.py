from playwright.sync_api import Page, expect

BASE_URL = "https://musicgate.co.il"


class BasePage:
    """Shared actions for every page object."""

    def __init__(self, page: Page):
        self.page = page
        self.preloader = page.locator("#martfury-preloader")

    def open(self, path: str = "/"):
        self.page.goto(f"{BASE_URL}{path}")
        self._wake_up_site()

    def _wake_up_site(self):
        # The site uses WP Rocket "delay JS": scripts (including the one that
        # removes the loading overlay) only run after user interaction.
        self.page.mouse.move(200, 200)
        self.page.mouse.wheel(0, 200)
        expect(self.preloader).to_be_hidden()

    def open_homepage(self):
        self.open("/")
