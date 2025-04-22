import re
from typing import Callable
from behave import given, when, then
from bdd.features.steps.utils import find_func_by_step, action, get_page, ARG, Priority


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

@action(f'{ARG} should be absent', priority=Priority.MEDIUM)
def assert_element_absent(context, element: str) -> None:
    context.current_page.assert_element_is_visible(element, False)

@action(f'should be {ARG}', priority=Priority.MEDIUM)
def assert_element_present(context, element: str) -> None:
    context.current_page.assert_element_is_visible(element, True)

@action('should be header elements')
def assert_header(context) -> None:
    context.current_page.assert_header()

    print('[DEBUG] Header elements checked')

@action(f'execute {ARG} on {ARG}')
def execute_context_element_method(context, method_name: str, context_element: str, *args) -> None:
    context_element_instance = getattr(context, context_element)

    if (method := getattr(context_element_instance, method_name, None)) is not None:
        if callable(method):
            method(*args)
        else:
            raise TypeError(f"'{method_name}' exists in {context_element_instance}, but is not callable.")
    else:
        raise TypeError(f"'{method_name}' is not exists in {context_element_instance}.")


@action(f'should be {ARG} on {ARG}', priority=Priority.MAJOR)
def assert_context_element_present(context, element: str, context_element: str) -> None:
    method_name = f'expect_{element}_visible'
    execute_context_element_method(context, method_name, context_element)

@action(f'{ARG} absent on {ARG}', priority=Priority.MAJOR)
def assert_context_element_present(context, element: str, context_element: str) -> None:
    method_name = f'expect_{element}_visible'
    execute_context_element_method(context, method_name, context_element, False)
