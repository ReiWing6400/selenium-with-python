from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_link.click()

    def get_item_name(self):
        item_name_el = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        item_name = item_name_el.text
        print(item_name)
        return item_name

    def get_added_item_name(self):
        added_item_name_el = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME)
        added_item_name = added_item_name_el.text
        print(added_item_name)
        return added_item_name

