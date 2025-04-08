from playwright.sync_api import Page, Locator

from playwright.sync_api import expect


class PageBase:
    url = None
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state('networkidle')

    @staticmethod
    def _check_element_text(element: Locator, text: str):
        expect(element).to_be_visible()
        assert element.text_content() == text, f'Text in {element} does not match "{text}"'