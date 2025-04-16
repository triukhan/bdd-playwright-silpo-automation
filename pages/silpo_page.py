from playwright.sync_api import Page

from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.locators import CATEGORY_HEAD_BTN, LOGO_HEAD, SEARCH_HEAD_BTN, GEO_HEAD_BTN, LOGIN_HEAD_BTN, \
    BURGER_HEAD_BTN
from pages.main_page.locators import SELECT_ADDRESS_DIALOG, SEARCH_ADDRESS_FIELD, ADDRESS_CONFIRM_BTN, \
    CLOSE_ADDRESS_CONFIRM, SEARCH_SUGGESTIONS, ADDRESS_LABEL

DELIVERY_ADDRESS = 'Київ, Глибочицька вулиця, 12'

class SilpoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.category_btn = self.page.locator(CATEGORY_HEAD_BTN)
        self.logo = self.page.locator(LOGO_HEAD)
        self.search_btn = self.page.locator(SEARCH_HEAD_BTN)
        self.geo_header_btn = self.page.locator(GEO_HEAD_BTN)
        self.login_btn = self.page.locator(LOGIN_HEAD_BTN)
        self.burger_button = self.page.locator(BURGER_HEAD_BTN)
        self.vacancies_link = self.page.get_by_role('link', name='Вакансії')
        self.select_address_dialog = self.page.locator(SELECT_ADDRESS_DIALOG)
        self.search_address_field = self.page.locator(SEARCH_ADDRESS_FIELD)
        self.address_confirm_button = self.page.locator(ADDRESS_CONFIRM_BTN)
        self.close_address_confirm_btn = self.page.locator(CLOSE_ADDRESS_CONFIRM)
        self.address_label = self.page.locator(ADDRESS_LABEL)

    def assert_header(self):
        expect(self.category_btn).to_be_visible()
        expect(self.logo).to_be_visible()
        expect(self.search_btn).to_be_visible()
        expect(self.geo_header_btn).to_be_visible()
        expect(self.login_btn).to_be_visible()
        expect(self.burger_button).to_be_visible()

    def set_delivery_address(self, address: str = DELIVERY_ADDRESS):
        self.geo_header_btn.click()
        self.search_address_field.fill(address)
        self.search_address_field.click()
        self.page.locator(SEARCH_SUGGESTIONS).first.click()
        self.address_confirm_button.click()
        expect(self.address_label).to_have_text(address, timeout=15000, use_inner_text=True)
