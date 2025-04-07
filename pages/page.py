from playwright.sync_api import Page, Locator

from playwright.sync_api import expect


class PageBase:
    def __init__(self, page: Page):
        self.page = page

    def _open(self, page_link: str):
        self.page.goto(page_link)
        self.page.wait_for_load_state('networkidle')

    @staticmethod
    def _check_element_text(element: Locator, text: str):
        expect(element).to_be_visible()
        assert element.text_content() == text, f'Text in {element} does not match "{text}"'