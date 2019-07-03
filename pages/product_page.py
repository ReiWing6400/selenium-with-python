from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ITEM_ADD_TO_BASKET_BUTTON)
        add_to_basket_link.click()

    def get_item_name(self):
        item_name_el = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        item_name = item_name_el.text
        return item_name

    def get_messages_added_item_name(self):
        messages_added_item_name_el = self.browser.find_element(*ProductPageLocators.MESSAGES_ADDED_ITEM_NAME)
        messages_added_item_name = messages_added_item_name_el.text
        return messages_added_item_name

    def get_item_price(self):
        item_price_el = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        item_price = str.strip(item_price_el.text)
        return item_price

    def get_messages_added_item_price(self):
        messages_added_item_price_el = self.browser.find_element(*ProductPageLocators.MESSAGES_ADDED_ITEM_PRICE)
        messages_added_item_price = str.strip(messages_added_item_price_el.text)
        return messages_added_item_price

    def get_header_basket_total_price(self):
        header_basket_total_price_el = self.browser.find_element(*BasePageLocators.HEADER_BASKET_TOTAL_PRICE)
        header_basket_total_price_text = str.strip(header_basket_total_price_el.text).split(":")[1].split("\n")[0]
        header_basket_total_price = str.strip(header_basket_total_price_text)
        return header_basket_total_price

    def should_be_product_main_form(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), "Item name is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), "Item price is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_OK_ICON), "Item Ok_icon is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_AVAILABILITY), "Item availability is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_ADD_TO_BASKET_BUTTON), \
            "Item add to basket button is not present"
        assert self.is_element_present(*ProductPageLocators.ITEM_ADD_TO_WISHLIST_BUTTON), \
            "Item add to wishlist button is not present"
        assert True

    def should_be_messages(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGES_OFFER), "Offer message is not present"
        assert self.is_element_present(*ProductPageLocators.MESSAGES_ADDED_ITEM_PRICE), \
            "Item price message is not present"
        assert self.is_element_present(*ProductPageLocators.MESSAGES_ADDED_ITEM_NAME), \
            "Item name message is not present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES_ADDED_ITEM_NAME), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGES_ADDED_ITEM_NAME), \
            "Success message is presented, but should disappeared"
