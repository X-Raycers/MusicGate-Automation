import allure
from playwright.sync_api import Page, expect


@allure.title("Navigate to percussion instruments main category")
def test_navigate_to_percussion_main_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator("#mega-menu-item-87484").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%aa%d7%95%d7%a4%d7%99%d7%9d-%d7%95%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(2000)


@allure.title("Navigate to darbukas category")
def test_navigate_to_darbukas_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87484 span.mega-indicator').click()
    page.locator("#mega-menu-item-87488").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%aa%d7%95%d7%a4%d7%99%d7%9d-%d7%95%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94-%d7%93%d7%a8%d7%91%d7%95%d7%a7%d7%94")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to bongos category")
def test_navigate_to_bongos_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87484 span.mega-indicator').click()
    page.locator("#mega-menu-item-88211").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%aa%d7%95%d7%a4%d7%99%d7%9d-%d7%95%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to xylophones category")
def test_navigate_to_xylophones_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87484 span.mega-indicator').click()
    page.locator("#mega-menu-item-88216").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%aa%d7%95%d7%a4%d7%99%d7%9d-%d7%95%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94/%d7%a7%d7%a1%d7%99%d7%9c%d7%95%d7%a4%d7%95%d7%a0%d7%99%d7%9d")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to wind instruments main category")
def test_navigate_to_wind_instruments_main_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator("#mega-menu-item-87506").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9b%d7%9c%d7%99-%d7%a0%d7%a9%d7%99%d7%a4%d7%94")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)



@allure.title("Navigate to harmonicas category")
def test_navigate_to_harmonicas_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87506 span.mega-indicator').click()
    page.locator("#mega-menu-item-87514").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9b%d7%9c%d7%99-%d7%a0%d7%a9%d7%99%d7%a4%d7%94/%d7%9e%d7%a4%d7%95%d7%97%d7%99%d7%95%d7%aa")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to melodicas category")
def test_navigate_to_melodicas_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87506 span.mega-indicator').click()
    page.locator("#mega-menu-item-87513").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9b%d7%9c%d7%99-%d7%a0%d7%a9%d7%99%d7%a4%d7%94/%d7%9e%d7%9c%d7%95%d7%93%d7%99%d7%a7%d7%95%d7%aa")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to kazoo category")
def test_navigate_to_kazoo_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87506 span.mega-indicator').click()
    page.locator("#mega-menu-item-87516").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9b%d7%9c%d7%99-%d7%a0%d7%a9%d7%99%d7%a4%d7%94/%d7%a7%d7%90%d7%96%d7%95")
    page.wait_for_timeout(2000)
    page.mouse.wheel(0, 3000)
    page.wait_for_timeout(3000)