from playwright.sync_api import Page, expect
from pages.main_page.main_page import MainPage
from pages.vacancies_page.vacancies_page import VacanciesPage


def test_check_header(main_page: MainPage):
    main_page.check_header()

def test_cookie_menu(main_page: MainPage):
    main_page.check_cookie_banner()
    main_page.accept_cookie.click()
    expect(main_page.cookie_banner).not_to_be_visible()

def test_goto_vacancies(main_page: MainPage, page: Page):
    main_page.burger_btn.click()
    main_page.vacancies_link.click()
    vacancies_page = VacanciesPage(page)
    expect(vacancies_page.vacancies_banner).to_be_visible()
    vacancies_page.check_header()
    vacancies_page.logo.click()
    expect(main_page.main_banner).to_be_visible()

def test_add_product_without_address(main_page: MainPage):
    main_page.get_first_product().click()
    expect(main_page.select_address_dialog).to_be_visible()


def test_add_product(main_page_with_address: MainPage):
    main_page = main_page_with_address
    product_card = main_page.get_first_product()
    product_card.add_to_cart()
    cart_count = main_page.get_cart_counter()
    assert cart_count == '1',  f'Expected cart count to be 1, but got {cart_count}'

def test_card_counter(main_page_with_address: MainPage):
    main_page = main_page_with_address
    product_card = main_page.get_first_product()
    product_card.add_to_cart()
    product_card.expect_counter_visible()
    product_card.decrease()
    product_card.expect_counter_visible(False)