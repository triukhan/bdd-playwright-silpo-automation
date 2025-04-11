from playwright.sync_api import Page, Locator

from playwright.sync_api import expect


class BasePage:
    url = None
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state('domcontentloaded')

    @staticmethod
    def _check_element_text(element: Locator, text: str):
        expect(element).to_be_visible()
        assert element.text_content() == text, f'Text in {element} does not match "{text}"'

    def click(self, element_name: str):
        getattr(self, element_name).click()

    def assert_element_is_visible(self, element_name: str, visible: bool = True):
        element = getattr(self, element_name)

        if visible:
            expect(element).to_be_visible()
        else:
            expect(element).not_to_be_visible()