import os

import pytest
from playwright.sync_api import Page

from pages.main_page.main_page import MainPage

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
STORAGE_PATH = os.path.join(BASE_DIR, 'storage')

@pytest.fixture
def main_page(page: Page):
    main_page = MainPage(page)
    main_page.open()
    return main_page

@pytest.fixture
def core(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    return browser, context, page

@pytest.fixture
def context_main_page_with_address(core):
    browser, context, page = core
    os.makedirs(STORAGE_PATH, exist_ok=True)
    state_path = os.path.join(STORAGE_PATH, 'main_page_address.json')

    if os.path.exists(state_path):
        print('[DEBUG] Session already exists, using existing')
        return state_path

    main_page = MainPage(page)
    main_page.open()
    main_page.set_delivery_address()

    context.storage_state(path=state_path)
    browser.close()
    print('[DEBUG] Session created and saved to file')

    return state_path

@pytest.fixture
def main_page_with_address(playwright, context_main_page_with_address):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=context_main_page_with_address)
    page = context.new_page()

    main_page = MainPage(page)
    main_page.open()

    yield main_page

    context.close()
    browser.close()
