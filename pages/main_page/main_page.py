from playwright.sync_api import Page

from pages.main_page.profuct_card import ProductCard
from pages.silpo_page import SilpoPage
from utils.links import MAIN_PAGE
from pages.main_page.locators import COOKIE_BANNER_TITLE, COOKIE_BANNER_ACCEPT, MAIN_BANNER, ADD_TO_CARD_BTN, \
    COUNT_CARD_BADGE, CAROUSEL
from utils.texts import COOKIE_TITLE


class MainPage(SilpoPage):
    url = MAIN_PAGE

    def __init__(self, page: Page):
        super().__init__(page)
        self.cookie_banner = self.page.locator(COOKIE_BANNER_TITLE)
        self.accept_cookie = self.page.locator(COOKIE_BANNER_ACCEPT)
        self.main_banner = self.page.locator(MAIN_BANNER)
        self.add_to_cart_buttons = self.page.locator(ADD_TO_CARD_BTN)
        self.count_cart_badge = self.page.locator(COUNT_CARD_BADGE)
        self._sales_carousel = self.page.locator(CAROUSEL)

    def get_cart_counter(self):
        return self.count_cart_badge.inner_text()

    def check_cookie_banner(self):
        self._check_element_text(self.cookie_banner, COOKIE_TITLE)

    def get_first_product(self) -> ProductCard:
        return ProductCard(self._sales_carousel.first)
