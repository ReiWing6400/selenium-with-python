from ..pages.login_page import LoginPage
from ..pages.main_page import MainPage
from ..pages.base_page import BasePage
from ..pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_basket_empty_text()
    basket_page.should_not_be_basket_items()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):


# Гость открывает страницу товара
# Переходит в корзину по кнопке в шапке
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста