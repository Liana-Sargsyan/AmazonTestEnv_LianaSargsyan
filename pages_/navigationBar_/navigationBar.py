from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__accountBoxLocator = (By.ID, "nav-link-accountList")
        self.__signOutLocator = (By.ID, "nav-item-signout")
        self.__cartButtonLocator = (By.ID, "nav-cart-count")
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchSubmitButtonLocator = (By.ID, "nav-search-submit-button")
        self.__cartCountValidationLocator = (By.ID, "nav-cart-count")

    def mouse_move_to_account_box(self):
        accountBoxElement = self._find_element(self.__accountBoxLocator)
        self._mouse_move(accountBoxElement)

    def click_to_sign_out_element(self):
        signOutElement = self._find_element(self.__signOutLocator)
        self._click_to_element(signOutElement)

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click_to_element(cartButtonElement)

    def fill_search_field(self, product):
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._fill_field(searchFieldElement, product)

    def click_to_search_submit_button(self):
        searchSubmitButtonElement = self._find_element(self.__searchSubmitButtonLocator)
        self._click_to_element(searchSubmitButtonElement)

    def get_cart_count(self):
        cartCountElement = self._find_element(self.__cartCountValidationLocator)
        return self._get_element_text(cartCountElement)

    def get_search_field_text(self):
        searchFieldTextElement = self._find_element(self.__searchFieldLocator)
        return self._get_element_text(searchFieldTextElement)
