import inspect
import re

from playwright.sync_api import Page

VALUES = {
    'true': True,
    'false': False,
}

ARG = r'(\w+)'

actions = {}

def get_page(page_name: str, page: Page):
    from pages.main_page.main_page import MainPage
    from pages.vacancies_page.vacancies_page import VacanciesPage
    pages = {'main': MainPage, 'vacancies': VacanciesPage}

    return pages[page_name](page)

def action(pattern: str):
    def decorator(func):
        regex = re.compile(pattern)
        actions[regex] = func
        return func
    return decorator

def parse_arg_value(value: str):
    found_value = VALUES.get(value)
    return found_value if found_value is not None else value

def find_func_by_step(step_parts: list):
    func_name = step_parts[0]
    args = step_parts[1:]
    kwargs = {}

    for regex, func in actions.items():
        match = regex.match(func_name)
        if match:
            for arg in args[:]:
                arg_list = arg.split(' ')
                if len(arg_list) == 1:
                    kwargs[arg_list[0]] = True
                if len(arg_list) == 2:
                    sig = inspect.signature(func)
                    if arg_list[0] in [param.name for param in sig.parameters.values()]:
                        kwargs[arg_list[0]] = parse_arg_value(arg_list[1])
                    else:
                        raise ValueError(f'Unexpected argument: {arg_list[0]}')
                args.remove(arg)

            return func, match.groups() + tuple(args), kwargs
    raise ValueError(f'No matching function for step: {step_parts}')