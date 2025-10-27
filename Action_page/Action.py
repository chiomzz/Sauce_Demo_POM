from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locator_page.Locators import LoginLocators, AddToCart, Payment, Logout


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.USERNAME))
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        password_field.send_keys(password)

    def click_login(self):
        login_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.LOGIN))
        login_field.click()



class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_backpack(self):
        backpack_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.SAUCE_LAB_BACKPACK))
        backpack_button.click()

    def click_backlight(self):
        backlight_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.SAUCE_LAB_BIKE_LIGHT))
        backlight_button.click()

    def click_bold_t_shirt(self):
        bold_t_shirt_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.SAUCE_LAB_BOLD_T_SHIRT))
        bold_t_shirt_button.click()

    def click_fleece_jacket(self):
        fleece_jacket_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.SAUCE_LAB_FLEECE_JACKET))
        fleece_jacket_button.click()

    def click_onesie(self):
        onesie_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.SAUCE_LAB_ONESIE))
        onesie_button.click()

    def click_all_things_t_shirt(self):
        all_things_t_shirt_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.TEST_ALL_THINGS_T_SHIRT))
        all_things_t_shirt_button.click()


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    def click_shopping_cart(self):
        shopping_cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(Payment.SHOPPING_CART))
        shopping_cart_button.click()

    def click_checkout(self):
        checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(Payment.CHECKOUT_BUTTON))
        checkout_button.click()

    def enter_firstname(self, firstname):
        firstname_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(Payment.FIRSTNAME))
        firstname_field.send_keys(firstname)

    def enter_lastname(self, lastname):
        lastname_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(Payment.LASTNAME))
        lastname_field.send_keys(lastname)

    def enter_zipcode(self, zipcode):
        zipcode_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(Payment.ZIPCODE))
        zipcode_field.send_keys(zipcode)

    def click_continue(self):
        continue_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(Payment.CONTINUE_BUTTON))
        continue_button.click()

    def click_finish(self):
        finish_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(Payment.FINISH_BUTTON))
        finish_button.click()



class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_burger_menu(self):
        burger_menu = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(Logout.BURGER_MENU))
        burger_menu.click()

    def click_logout(self):
        logout = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(Logout.LOGOUT_BUTTON))
        logout.click()