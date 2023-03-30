import pytest
import os

from playwright.sync_api import Page, expect

base_url = os.environ['BASE_URL']


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}


def test_example(page: Page) -> None:
    page.goto(base_url)
    page.locator(".sc-7fa25ec4-0 > a:nth-child(3)").click()
    page.get_by_role("button", name="Register here").click()
    page.get_by_role("textbox").first.click()
    page.get_by_role("textbox").first.fill("test")
    page.get_by_role("button", name="Register").click()
    error = page.get_by_text("Invalid email address")
    expect(error).to_have_text("Invalid email address")