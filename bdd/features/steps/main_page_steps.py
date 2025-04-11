from bdd.features.steps.utils import action


@action('should be header elements')
def assert_header(context) -> None:
    context.current_page.check_header()

    print('[DEBUG] Header elements checked')


@action('should be cookie banner')
def assert_cookie_menu(context) -> None:
    context.current_page.check_cookie_banner()