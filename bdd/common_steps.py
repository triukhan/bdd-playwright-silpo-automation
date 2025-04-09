from behave import given
from pages.main_page.main_page import MainPage
from functools import wraps

PAGES = {'main': MainPage}


def parse_modifiers(func):
    @wraps(func)
    def wrapper(context, page_name: str, modifiers: str = ''):
        full_text = context.text or ''
        print(modifiers)

        options = {
            'with_delivery': 'with delivery' in full_text,
            'with_login': 'with login' in full_text,
        }

        return func(context, page_name, **options)

    return wrapper


@given('open {page_name} page{modifiers:Optional}')
@parse_modifiers
def open_page(context, page_name: str, with_delivery: bool = False):
    page_class = PAGES[page_name](context.page)
    page_class.open()
    if with_delivery:
        page_class.set_delivery_address()