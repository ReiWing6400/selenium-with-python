from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket is not present in current url"
        assert True

    def should_be_basket_empty_text(self):
        basket_empty_el = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT)
        basket_empty_text = basket_empty_el.text
        assert basket_empty_text == 'Your basket is empty.', "Basket isn't empty, but should be"
        assert True

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be"
