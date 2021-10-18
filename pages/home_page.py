from selenium.webdriver.common.by import By
from lib import conf_reader


class HomePage:

    def __init__(self, obj):
        global driver
        driver = obj

    def product_selection(self, product, price):
        # Assertion for checking cart should be empty before adding a product
        assert len(driver.find_elements(By.XPATH, conf_reader.fetch_home_page_elements_locators('HomePage', 'cart_badge'))) ==0

        product_add_to_cart = driver.find_element(By.XPATH, conf_reader.fetch_home_page_elements_locators('HomePage', 'add_to_cart_button'))
        product_add_to_cart.click()

        # Assert remove button is shown in place of add to cart
        assert driver.find_elements(By.XPATH, conf_reader.fetch_home_page_elements_locators('HomePage', 'remove_button'))

        # Assertion for checking cart should have just one product added
        assert len(driver.find_elements(By.XPATH,
                                        conf_reader.fetch_home_page_elements_locators('HomePage', 'cart_badge'))) == 1

    def shopping_cart_navigate(self):
        cart_button = driver.find_element(By.XPATH, conf_reader.fetch_home_page_elements_locators('HomePage', 'cart_button'))
        cart_button.click()

