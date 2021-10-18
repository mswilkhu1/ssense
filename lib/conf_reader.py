import configparser


def read_config_data(section, key):
    config = configparser.ConfigParser()
    config.read('./config.cfg')
    return config.get(section, key)


def fetch_login_page_elements_locators(section, key):
    config = configparser.ConfigParser()
    config.read('./selectors/login_page.cfg')
    return config.get(section, key)


def fetch_home_page_elements_locators(section, key):
    config = configparser.ConfigParser()
    config.read('./selectors/home_page.cfg')
    return config.get(section, key)


def fetch_checkout_pages_elements_locators(section, key):
    config = configparser.ConfigParser()
    config.read('./selectors/checkout_pages.cfg')
    return config.get(section, key)
