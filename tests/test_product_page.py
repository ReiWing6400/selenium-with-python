from ..pages.product_page import ProductPage
from ..pages.login_page import LoginPage
import pytest


@pytest.mark.login_guest
class TestGuestLoginFromProductPage(object):
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        login_page.should_be_login_form()
        login_page.should_be_register_form()


@pytest.mark.add_to_cart_guest
class TestGuestAddToCartFromProductPage(object):
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_cart(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_main_form()
        page.should_not_be_success_message()
        item_price = page.get_item_price()
        item_name = page.get_item_name()
        page.click_add_to_basket()
        page.solve_quiz_and_get_code()
        header_basket_total_price = page.get_header_basket_total_price()
        page.should_be_messages()
        messages_added_item_name = page.get_messages_added_item_name()
        messages_add_item_price = page.get_messages_added_item_price()
        page.is_elements_match(item_name, messages_added_item_name)
        page.is_elements_match(item_price, messages_add_item_price)
        page.is_elements_match(item_price, header_basket_total_price)

    def test_guest_cant_see_success_message_after_adding_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket()
        page.should_not_be_success_message()


@pytest.mark.add_to_card_user
class TestUserAddToCartFromProductPage(object):
