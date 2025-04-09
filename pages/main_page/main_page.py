from dataclasses import dataclass

from playwright.sync_api import Page, expect, Locator

from pages.silpo_page import SilpoPage
from utils.links import MAIN_PAGE
from pages.main_page.locators import COOKIE_BANNER_TITLE, COOKIE_BANNER_ACCEPT, MAIN_BANNER, ADD_TO_CARD_BTN, \
    COUNT_CARD_BADGE, CAROUSEL, ADD_TO_CART_ICON, DECREASE_ICON
from utils.texts import COOKIE_TITLE


class MainPage(SilpoPage):
    url = MAIN_PAGE

    def __init__(self, page: Page):
        super().__init__(page)
        self.cookie_banner_title = self.page.locator(COOKIE_BANNER_TITLE)
        self.cookie_banner_accept = self.page.locator(COOKIE_BANNER_ACCEPT)
        self.main_banner = self.page.locator(MAIN_BANNER)
        self.add_to_cart_buttons = self.page.locator(ADD_TO_CARD_BTN)
        self.count_cart_badge = self.page.locator(COUNT_CARD_BADGE)
        self._sales_carousel = self.page.locator(CAROUSEL)

    def get_cart_counter(self):
        return self.count_cart_badge.inner_text()

    def check_cookie_banner(self):
        self._check_element_text(self.cookie_banner_title, COOKIE_TITLE)

    def get_first_product(self):
        return ProductCard(self._sales_carousel.first)

@dataclass
class ProductCard:
    element: Locator
    cart_counter: int = 0

    def __post_init__(self):
        self.info: str = self.element.text_content()
        self.add_button: Locator = self.element.locator(ADD_TO_CARD_BTN)
        self.add_icon: Locator = self.element.locator(ADD_TO_CART_ICON)
        self.decrease_icon: Locator = self.element.locator(DECREASE_ICON)

    def add_to_cart(self):
        if not self.cart_counter:
            self.add_button.click()
            self.cart_counter += 1
        else:
            self.add_icon.click()

    def decrease(self):
        if not self.cart_counter:
            raise ValueError('The product is not added to the cart')
        self.decrease_icon.click()

    def expect_counter_visible(self, visible: bool = True):
        if visible:
            expect(self.add_icon).to_be_visible()
            expect(self.decrease_icon).to_be_visible()
            expect(self.add_button).not_to_be_visible()
        else:
            expect(self.add_icon).not_to_be_visible()
            expect(self.decrease_icon).not_to_be_visible()
            expect(self.add_button).to_be_visible()