import pytest
from playwright.sync_api import Page

from pages.main_page.main_page import MainPage


@pytest.fixture
def main_page(page: Page):
    main_page = MainPage(page)
    main_page.open()
    return main_page

@pytest.fixture
def main_page_with_address(main_page: MainPage):
    main_page.set_delivery_address()
    return main_page
