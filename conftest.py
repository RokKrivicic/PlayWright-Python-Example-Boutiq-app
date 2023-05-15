"""pytest: unit and functional testing with Python."""
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    iphone_13 = playwright.devices["iPhone 13"]
    return {
        **browser_context_args,
        **iphone_13,
    }
