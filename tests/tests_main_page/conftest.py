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
    main_page.add_to_cart_buttons.first.click()
    main_page.search_address_field.fill('глибочицька, 12')
    main_page.search_address_field.click()
    main_page.click_first_suggested_address()
    main_page.address_confirm_button.click()
    return main_page
