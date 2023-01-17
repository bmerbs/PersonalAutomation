from playwright.sync_api import Playwright, sync_playwright, expect


def enterInfo(page, username = str, password = str):
    page.locator("#responsive_page_template_content input[type=\"text\"]").fill("Testing505Test")
    page.locator("input[type=\"password\"]").click()
    page.locator("input[type=\"password\"]").fill("PlaywrightPass123")
    page.get_by_role("button", name="Sign in").click()