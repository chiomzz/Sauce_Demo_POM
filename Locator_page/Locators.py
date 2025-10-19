from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN = (By.ID, 'login-button')

class AddToCart:
    SAUCE_LAB_BACKPACK = (By.ID, 'remove-sauce-labs-backpack')
    SAUCE_LAB_BIKE_LIGHT = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    SAUCE_LAB_BOLD_T_SHIRT = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    SAUCE_LAB_FLEECE_JACKET = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    SAUCE_LAB_ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    TEST_ALL_THINGS_T_SHIRT = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')

class Payment:
    SHOPPING_CART = (By.CSS_SELECTOR, '#shopping_cart_container > a')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#checkout')
    FIRSTNAME = (By.XPATH, '//*[@id="first-name"]')
    LASTNAME = (By.XPATH, '//*[@id="last-name"]')
    ZIPCODE = (By.XPATH, '//*[@id="postal-code"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="continue"]')
    FINISH_BUTTON = (By.XPATH, '//*[@id="finish"]')

class Logout:
    BURGER_MENU = (By.CSS_SELECTOR, '#react-burger-menu-btn')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#logout_sidebar_link')






