from lib import conf_reader
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, obj):
        global driver
        driver = obj

    def user_login(self):
        user = conf_reader.read_config_data('Details', 'Username')
        password = conf_reader.read_config_data('Details', 'Password')

        username_input = driver.find_element(By.XPATH, conf_reader.fetch_login_page_elements_locators('LoginPage', 'username'))
        username_input.send_keys(user)

        password_input = driver.find_element(By.XPATH,
                                             conf_reader.fetch_login_page_elements_locators('LoginPage', 'password'))
        password_input.send_keys(password)

        login_button = driver.find_element(By.XPATH,
                                             conf_reader.fetch_login_page_elements_locators('LoginPage', 'login_button'))
        login_button.click()
