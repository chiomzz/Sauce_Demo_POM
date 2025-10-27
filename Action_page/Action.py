from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locator_page.Locators import LoginLocators, AddToCart


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

    def click_backpack(self, backpack):
        backpack_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.SAUCE_LAB_BACKPACK))
        backpack_button.click()

    def click_backlight(self, backlight):
        backlight_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.SAUCE_LAB_BIKE_LIGHT))
        backlight_button.click()

    def click_bold_t_shirt(self, bold_t_shirt):
        bold_t_shirt_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.SAUCE_LAB_BOLD_T_SHIRT))
        bold_t_shirt_button.click()

    def click_fleece_jacket(self, fleece_jacket):
        fleece_jacket_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.SAUCE_LAB_FLEECE_JACKET))
        fleece_jacket_button.click()

    def click_onesie(self, onesie):
        onesie_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.SAUCE_LAB_ONESIE))
        onesie_button.click()

    def click_all_things_t_shirt(self, all_things_t_shirt):
        all_things_t_shirt_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCart.TEST_ALL_THINGS_T_SHIRT))
        all_things_t_shirt_button.click()