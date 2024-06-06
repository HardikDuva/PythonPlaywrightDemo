import re
from playwright.sync_api import Page, expect


def test_navigate(page: Page):
    # Expect a title "to contain" a substring.
    page.goto("https://www.flipkart.com/")

    expect(page.locator("//a[@title='Cart'][1]")).to_be_visible()

    page.locator("//a[@title='Cart'][1]").click()

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Shopping Cart"))
