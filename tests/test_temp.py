import time

from playwright.sync_api import Page, expect

from pages.main_page import MainPage


def test_check_header(page: Page):
    main_page = MainPage(page)
    main_page.open()
    main_page.check_header()

def test_cookie_menu(page: Page):
    main_page = MainPage(page)
    main_page.open()
    main_page.check_cookie_banner()
    main_page.cookie_banner_accept.click()
    assert not main_page.cookie_banner_title.is_visible(), 'The cookie banner is not disappeared'

def test_invalid_login_number(page: Page):
    main_page = MainPage(page)
    main_page.open()
    main_page.login_button.click()
    main_page.number_field.fill('0')