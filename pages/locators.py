from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators(object):
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_RESET_PASSWORD = (By.CSS_SELECTOR, "a[href$='/password-reset/']")
    LOGIN_SUBMIT_BUTTON = (By.NAME, "login_submit")

    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators(object):
    # HEADER_BASKET_TOTAL_PRICE =

    ITEM_NAME = (By.CSS_SELECTOR, "div[class$='product_main'] > h1")
    ITEM_PRICE = (By.CSS_SELECTOR, "div[class$='product_main'] > .price_color")
    ITEM_OK_ICON = (By.CSS_SELECTOR, "div[class$='product_main'] i[class='icon-ok']")
    ITEM_AVAILABILITY = (By.CSS_SELECTOR, "div[class$='product_main'] p.instock.availability")
    ITEM_SEND_FEEDBACK_BUTTON = (By.CSS_SELECTOR, "#write_review")
    ITEM_ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    ITEM_ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, "button[class$='wishlist']")

    MESSAGES_ADDED_ITEM_NAME = (By.XPATH, "//*[text()[contains(.,'added')]]/strong")
    MESSAGES_ADDED_ITEM_PRICE = (By.XPATH, "//*[text()[contains(.,'basket total')]]/strong")
