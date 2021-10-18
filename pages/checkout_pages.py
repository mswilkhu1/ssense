from selenium.webdriver.common.by import By

from lib import conf_reader


class CheckoutPages:

    def __init__(self, obj):
        global driver
        driver = obj

    def assert_product_info(self, product, price):
        item_name = driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages', 'inventory_item_name'))
        # Asserting product name, price and quantity
        assert item_name.text == product

        item_price = driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages', 'inventory_item_price')).text
        if not price in item_price:
            raise AssertionError()

        cart_quantity = driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages', 'cart_quantity')).text
        assert cart_quantity == "1"

    def assert_total(self, price):
        item_price = driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages', 'subtotal')).text
        if not price in item_price:
            raise AssertionError()

    def click_checkout_button(self):
        checkout_button = driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages', 'checkout_button'))
        checkout_button.click()

    def enter_checkout_info(self, fname, lname, pcode):
        first_name = driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages', 'first_name'))
        first_name.send_keys(fname)

        last_name = driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages',
                                                                                                      'last_name'))
        last_name.send_keys(lname)

        postal_code = driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages',
                                                                                                      'postal'))
        postal_code.send_keys(pcode)

    def click_continue(self):
        continue_button = driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages', 'continue_button'))
        continue_button.click()

    def click_finish(self):
        finish_button = driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages', 'finish_button'))
        finish_button.click()

    def assert_confirmation_messages(self):
        assert driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages', 'title_confirmation_message'))

        assert driver.find_element(By.XPATH, conf_reader.fetch_checkout_pages_elements_locators('CheckoutPages',
                                                                                            'order_confirmation_message'))