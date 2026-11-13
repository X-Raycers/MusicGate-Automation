import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://musicgate.co.il"
CLOUDFLARE_TEXT = "Performing security verification"


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.preloader = page.locator("#martfury-preloader")

    def open(self, path: str = "/"):
        self.page.goto(f"{BASE_URL}{path}")
        self._skip_if_blocked_by_cloudflare()
        self._wake_up_site()

    def _skip_if_blocked_by_cloudflare(self):
        # Cloudflare sometimes blocks cloud servers (like GitHub Actions)
        # and shows a "security verification" page instead of the site.
        # We don't try to bypass it - we skip the test with a clear reason.
        if self.page.get_by_text(CLOUDFLARE_TEXT).count() > 0:
            pytest.skip("Blocked by Cloudflare bot protection (happens on CI servers)")

    def _wake_up_site(self):
        # WP Rocket delay JS: scripts run only after user interaction.
        # Sometimes the first interaction is too early and gets missed,
        # so we try up to 3 times.
        for attempt in range(3):
            self.page.mouse.move(200 + attempt * 50, 200)
            self.page.mouse.wheel(0, 200)
            try:
                expect(self.preloader).to_be_hidden(timeout=10_000)
                return
            except AssertionError:
                continue
        expect(self.preloader).to_be_hidden()

    def open_homepage(self):
        self.open("/")