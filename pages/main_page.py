from playwright.sync_api import Page, expect

from pages.page import PageBase
from utils.links import MAIN_PAGE
from utils.locators import CATEGORY_HEAD_BUTTON, CATEGORY_HEAD_ITEM, LOGO_HEAD, SEARCH_HEAD_BUTTON, GEO_HEAD_BUTTON, \
    LOGIN_HEAD_BUTTON, \
    BURGER_HEAD_BUTTON, COOKIE_BANNER_TITLE, COOKIE_BANNER_ACCEPT, NUMBER_FIELD
from utils.texts import COOKIE_TITLE


class MainPage(PageBase):
    def __init__(self, page: Page):
        super().__init__(page)
        self.category_button = self.page.locator(CATEGORY_HEAD_BUTTON)
        self.category_item = self.page.locator(CATEGORY_HEAD_ITEM)
        self.logo = self.page.locator(LOGO_HEAD)
        self.search_button = self.page.locator(SEARCH_HEAD_BUTTON)
        self.geo_header_button = self.page.locator(GEO_HEAD_BUTTON)
        self.login_button = self.page.locator(LOGIN_HEAD_BUTTON)
        self.burger_button = self.page.locator(BURGER_HEAD_BUTTON)
        self.cookie_banner_title = self.page.locator(COOKIE_BANNER_TITLE)
        self.cookie_banner_accept = self.page.locator(COOKIE_BANNER_ACCEPT)
        self.number_field = self.page.get_by_role('textbox', name='Телефон')

    def open(self):
        self._open(MAIN_PAGE)

    def check_header(self):
        expect(self.category_button).to_be_visible()
        expect(self.logo).to_be_visible()
        expect(self.search_button).to_be_visible()
        expect(self.geo_header_button).to_be_visible()
        expect(self.login_button).to_be_visible()
        expect(self.burger_button).to_be_visible()

    def check_cookie_banner(self):
        self._check_element_text(self.cookie_banner_title, COOKIE_TITLE)
