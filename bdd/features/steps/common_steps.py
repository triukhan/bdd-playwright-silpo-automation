import re
from typing import Callable
from behave import given, when, then
from bdd.features.steps.utils import find_func_by_step, action, get_page, ARG


@given('{text}')
@when('{text}')
@then('{text}')
def perform_step(context, text: str) -> Callable:
    step_parts = re.split(r',\s*| and | with ', text.lower().strip())
    func, args, kwargs = find_func_by_step(step_parts)
    return func(context, *args, **kwargs)


@action(f'open {ARG} page')
def open_page(context, page_name: str, delivery: bool = False) -> None:
    context.current_page = get_page(page_name, context.page)
    context.current_page.open()

    if delivery:
        context.current_page.set_delivery_address()

    print(f'[DEBUG] Opened {page_name} | delivery={delivery}')

@action(f'opened {ARG} page')
def opened_page(context, page_name: str) -> None:
    context.current_page = get_page(page_name, context.page)

    print(f'[DEBUG] New current page={page_name}')


@action(f'click {ARG}')
def click_element(context, element: str) -> None:
    context.current_page.click(element)

@action(f'{ARG} should be absent', priority=1)
def assert_element_absent(context, element: str) -> None:
    context.current_page.assert_element_is_visible(element, False)

@action(f'should be {ARG}', priority=1)
def assert_element_present(context, element: str) -> None:
    context.current_page.assert_element_is_visible(element, True)

@action('should be header elements')
def assert_header(context) -> None:
    context.current_page.assert_header()

    print('[DEBUG] Header elements checked')