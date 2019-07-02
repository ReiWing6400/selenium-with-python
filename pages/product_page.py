from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ITEM_ADD_TO_BASKET_BUTTON)
        add_to_basket_link.click()

    def get_item_name(self):
        item_name_el = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        item_name = item_name_el.text
        return item_name

    def get_added_item_name(self):
        added_item_name_el = self.browser.find_element(*ProductPageLocators.MESSAGES_ADDED_ITEM_NAME)
        added_item_name = added_item_name_el.text
        return added_item_name

    def get_item_price(self):
        item_price_el = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        item_price = item_price_el.text
        return item_price

    def should_be_product_main_form(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), "Item name is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), "Item price is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_OK_ICON), "Item Ok_icon is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_AVAILABILITY), "Item availability is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_ADD_TO_BASKET_BUTTON), "Item add to basket button is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_ADD_TO_WISHLIST_BUTTON), "Item add to wishlist button is not present"
        assert True
