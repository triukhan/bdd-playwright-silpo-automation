from bdd.features.steps.utils import action


@action('should be cookie banner')
def assert_cookie_menu(context) -> None:
    context.current_page.check_cookie_banner()