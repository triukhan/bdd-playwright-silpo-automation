from playwright.sync_api import Page, Locator

from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.locators import CATEGORY_HEAD_BTN, LOGO_HEAD, SEARCH_HEAD_BTN, GEO_HEAD_BTN, LOGIN_HEAD_BTN, \
    BURGER_HEAD_BTN


class SilpoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.category_btn = self.page.locator(CATEGORY_HEAD_BTN)
        self.logo = self.page.locator(LOGO_HEAD)
        self.search_btn = self.page.locator(SEARCH_HEAD_BTN)
        self.geo_header_btn = self.page.locator(GEO_HEAD_BTN)
        self.login_btn = self.page.locator(LOGIN_HEAD_BTN)
        self.burger_btn = self.page.locator(BURGER_HEAD_BTN)
        self.vacancies_link = self.page.get_by_role('link', name='Вакансії')

    def check_header(self):
        expect(self.category_btn).to_be_visible()
        expect(self.logo).to_be_visible()
        expect(self.search_btn).to_be_visible()
        expect(self.geo_header_btn).to_be_visible()
        expect(self.login_btn).to_be_visible()
        expect(self.burger_btn).to_be_visible()
