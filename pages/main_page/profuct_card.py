from dataclasses import dataclass

from playwright.sync_api import expect, Locator

from pages.main_page.locators import ADD_TO_CARD_BTN, ADD_TO_CART_ICON, DECREASE_ICON


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