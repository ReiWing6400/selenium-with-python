from ..pages.product_page import ProductPage
from ..pages.login_page import LoginPage
from ..pages.basket_page import BasketPage
import pytest
import time


@pytest.mark.login_guest
class TestGuestLoginFromProductPage(object):
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
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
    @pytest.mark.need_review
    def test_guest_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_main_form()
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

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_cart_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_url()
        basket_page.should_be_basket_empty_text()
        basket_page.should_not_be_basket_items()


@pytest.mark.add_to_cart_user
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "Test_123456"
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_registration_confirmation()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_main_form()
        page.should_be_wishlist_button_clickable_for_user()
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

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.should_not_be_success_message()
