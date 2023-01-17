from playwright.sync_api import Playwright, sync_playwright, expect
import steam_poms.steamhomepage as hp
import steam_poms.steamloginpage as lp

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    hp.signin(page)
    lp.enterInfo(page, "Testing505Test", "PlaywrightPass123")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
