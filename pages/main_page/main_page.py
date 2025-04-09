from playwright.sync_api import Page

from pages.silpo_page import SilpoPage
from utils.links import MAIN_PAGE
from pages.main_page.locators import COOKIE_BANNER_TITLE, COOKIE_BANNER_ACCEPT, MAIN_BANNER, ADD_TO_CARD_BTN, \
    SELECT_ADDRESS_DIALOG, SEARCH_ADDRESS_FIELD, SEARCH_SUGGESTIONS, ADDRESS_CONFIRM_BTN, CLOSE_ADDRESS_CONFIRM, \
    COUNT_CARD_BADGE
from utils.texts import COOKIE_TITLE


class MainPage(SilpoPage):
    url = MAIN_PAGE

    def __init__(self, page: Page):
        super().__init__(page)
        self.cookie_banner_title = self.page.locator(COOKIE_BANNER_TITLE)
        self.cookie_banner_accept = self.page.locator(COOKIE_BANNER_ACCEPT)
        self.main_banner = self.page.locator(MAIN_BANNER)
        self.add_to_cart_buttons = self.page.locator(ADD_TO_CARD_BTN)
        self.select_address_dialog = self.page.locator(SELECT_ADDRESS_DIALOG)
        self.search_address_field = self.page.locator(SEARCH_ADDRESS_FIELD)
        self.address_confirm_button = self.page.locator(ADDRESS_CONFIRM_BTN)
        self.close_address_confirm_btn = self.page.locator(CLOSE_ADDRESS_CONFIRM)
        self.count_cart_badge = self.page.locator(COUNT_CARD_BADGE)

    def get_cart_counter(self):
        return self.count_cart_badge.inner_text()

    def check_cookie_banner(self):
        self._check_element_text(self.cookie_banner_title, COOKIE_TITLE)

    def click_first_suggested_address(self):
        self.page.locator(SEARCH_SUGGESTIONS).first.click()
