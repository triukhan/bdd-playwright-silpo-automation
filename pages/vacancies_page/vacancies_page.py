from playwright.sync_api import Page

from pages.vacancies_page.locators import CATEGORY_HEAD_BTN, VACANCIES_BANNER, LOGO_HEAD, SEARCH_HEAD_BTN, GEO_HEAD_BTN, \
    LOGIN_HEAD_BTN, BURGER_HEAD_BTN
from pages.silpo_page import SilpoPage
from utils.links import VACANCIES_PAGE


class VacanciesPage(SilpoPage):
    url = VACANCIES_PAGE

    def __init__(self, page: Page):
        super().__init__(page)
        self.vacancies_banner = self.page.locator(VACANCIES_BANNER)
        self.category_btn = self.page.locator(CATEGORY_HEAD_BTN)
        self.logo = self.page.locator(LOGO_HEAD)
        self.search_btn = self.page.locator(SEARCH_HEAD_BTN)
        self.geo_header_btn = self.page.locator(GEO_HEAD_BTN)
        self.login_btn = self.page.locator(LOGIN_HEAD_BTN)
        self.burger_btn = self.page.locator(BURGER_HEAD_BTN)

