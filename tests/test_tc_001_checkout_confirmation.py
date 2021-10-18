import pytest
from pytest_bdd import scenario, given, when, then
from base import initiate_driver
from pages import login_page
from pages import home_page
from pages import checkout_pages


@pytest.fixture()
def browser():
    global driver
    driver = initiate_driver.start_browser()

    yield driver
    initiate_driver.close_browser()


@scenario("../features/product_checkout.feature", 'Ordering product on SwagLabs and getting confirmation')
def test_ordering_product_on_swaglabs_and_getting_confirmatoin(browser):
    """Ordering product on SwagLabs and getting confirmation"""


@given('user is logged in on SwagLabs')
def user_is_logged_in_on_SwagLabs():
    login = login_page.LoginPage(driver)
    login.user_login()

@when('user add to cart this <product> with <price>')
def user_add_to_cart_this_product_with_price(product, price):
    home = home_page.HomePage(driver)
    home.product_selection(product, price)

@when('user navigates to cart')
def user_navigates_to_cart():
    footwear = home_page.HomePage(driver)
    footwear.shopping_cart_navigate()

@when('clicks on checkout button')
def clicks_on_checkout_button():
    checkout = checkout_pages.CheckoutPages(driver)
    checkout.click_checkout_button()

@when('enter checkout information')
def enter_checkout_information():
    checkout_information = checkout_pages.CheckoutPages(driver)
    checkout_information.enter_checkout_info("test", "test", "test")

@when('click continue')
def click_continue():
    continue_button = checkout_pages.CheckoutPages(driver)
    continue_button.click_continue()

@when('click finish')
def click_finish():
    finish_button = checkout_pages.CheckoutPages(driver)
    finish_button.click_finish()

@then('confirmation should be displayed <price>')
def confirmation_should_be_displayed_price(price):
    confirmation = checkout_pages.CheckoutPages(driver)
    confirmation.assert_confirmation_messages()
