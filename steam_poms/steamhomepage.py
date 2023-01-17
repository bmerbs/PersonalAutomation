from playwright.sync_api import Playwright, sync_playwright, expect


#def signin(playwright: Playwright) -> None:
#    browser = playwright.chromium.launch(headless=False)
#    context = browser.new_context()
#    page = context.new_page()
#    page.goto("https://store.steampowered.com/")
#    page.locator("#global_action_menu").get_by_role("link", name="login").click()

def signin(page):
    page.goto("https://store.steampowered.com/")
    page.locator("#global_action_menu").get_by_role("link", name="login").click()