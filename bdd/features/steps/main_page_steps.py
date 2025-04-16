from bdd.features.steps.utils import action, ARG


@action('should be cookie banner')
def assert_cookie_menu(context) -> None:
    context.current_page.check_cookie_banner()

@action('add product')
def add_first_product(context) -> None:
    product_card = context.current_page.get_first_product()
    product_card.add_to_cart()

    print('[DEBUG] Added first product')

@action(f'cart counter should be {ARG}')
def asser_cart_counter(context, number: int) -> None:
    cart_count = context.current_page.get_cart_counter()
    assert cart_count == str(number),  f'Expected cart count to be 1, but got {cart_count}'