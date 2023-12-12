from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__accountBoxLocator = (By.ID, "nav-link-accountList")
        self.__signOutLocator = (By.ID, "nav-item-signout")

    def mouse_move_to_account_box(self):
        accountBoxElement = self._find_element(self.__accountBoxLocator)
        self._mouse_move(accountBoxElement)

    def click_to_sign_out_element(self):
        signOutElement = self._find_element(self.__signOutLocator)
        self._click_to_element(signOutElement)
