import re
from playwright.sync_api import Page, expect


def test_navigate(page: Page):
    # Expect a title "to contain" a substring.
    page.goto("https://playwright.dev/")

    locator = page.get_by_role("link", name="Get started")

    locator.click()

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Installation"))
