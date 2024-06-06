import re
from playwright.sync_api import Page, expect


def test_navigate(page: Page):
    # Expect a title "to contain" a substring.
    page.goto("https://www.amazon.in/")

    page.click("[id = 'nav-orders']")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Amazon Sign In"))
