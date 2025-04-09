import time

import pytest
from playwright.sync_api import Page

from pages.main_page.main_page import MainPage

DELIVERY_ADDRESS = 'Київ, Глибочицька вулиця, 12'

@pytest.fixture
def main_page(page: Page):
    main_page = MainPage(page)
    main_page.open()
    return main_page

@pytest.fixture
def main_page_with_address(main_page: MainPage):
    main_page.add_to_cart_buttons.first.click()
    main_page.search_address_field.fill(DELIVERY_ADDRESS)
    main_page.search_address_field.click()
    main_page.click_first_suggested_address()
    main_page.address_confirm_button.click()
    main_page.wait_for_address(DELIVERY_ADDRESS)
    return main_page
