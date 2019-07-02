from ..pages.product_page import ProductPage
import time


def test_guest_can_add_item_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    item_name = page.get_item_name()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    added_item_name = page.get_added_item_name()
    page.is_elements_match(item_name, added_item_name)
