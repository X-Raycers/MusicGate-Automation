import pytest
from playwright.sync_api import expect

# MusicGate is a slow site: allow more time, but only wait as long as needed
expect.set_options(timeout=15_000)


@pytest.fixture(autouse=True)
def slow_site_timeouts(page):
    page.set_default_timeout(30_000)
    page.set_default_navigation_timeout(45_000)
