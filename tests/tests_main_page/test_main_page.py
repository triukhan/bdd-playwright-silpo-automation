import time

from playwright.sync_api import Page, expect

from pages.main_page.main_page import MainPage
from pages.vacancies_page.vacancies_page import VacanciesPage


def test_check_header(main_page: MainPage):
    main_page.check_header()

def test_cookie_menu(main_page: MainPage):
    main_page.check_cookie_banner()
    main_page.cookie_banner_accept.click()
    expect(main_page.cookie_banner_title).not_to_be_visible()

def test_goto_vacancies(main_page: MainPage, page: Page):
    main_page.burger_btn.click()
    main_page.vacancies_link.click()
    vacancies_page = VacanciesPage(page)
    expect(vacancies_page.vacancies_banner).to_be_visible()
    vacancies_page.check_header()
    vacancies_page.logo.click()
    expect(main_page.main_banner).to_be_visible()

def test_add_goods_without_address(main_page: MainPage):
    main_page.add_to_cart_buttons.first.click()
    expect(main_page.select_address_dialog).to_be_visible()


def test_add_goods(main_page_with_address: MainPage):
    main_page = main_page_with_address
    time.sleep(1) # todo: in fixture add wait until address is aplied
    main_page.page.wait_for_selector('[aria-label^="Продукт"]')
    product_name = "Вершки Галичина ультрапастеризовані 15%"
    product_card = main_page.page.locator(f'[aria-label*="{product_name}"]').first
    price_locator = product_card.locator('.product-card-price__displayPrice')
    price_text = price_locator.inner_text()
    add_button = product_card.locator('[data-autotestid="card-add-to-basket-button"]')
    add_button.click()
    assert main_page.get_cart_counter() == '1'