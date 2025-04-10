import re
from typing import Callable
from behave import given

from bdd.features.steps.utils import find_func_by_step, action, get_page


@given('{step_text}')
def perform_step(context, step_text: str) -> Callable:
    step_parts = re.split(r',\s*| and | with ', step_text.lower().strip())
    func, args, kwargs = find_func_by_step(step_parts)
    return func(context, *args, **kwargs)


@action(r'open (\w+) page')
def open_page(context, page_name: str, delivery: bool = False) -> None:
    page_class = get_page(page_name, context.page)
    page_class.open()

    if delivery:
        page_class.set_delivery_address()

    print(f'[DEBUG] Opened {page_name} | delivery={delivery}')
