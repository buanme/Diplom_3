from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from urls import Urls


class PersonalAccountPage(BasePage):

    @allure.step("Клик по 'Личный кабинет'")
    def click_lk_button(self):
        self.click((By.XPATH, PersonalAccountLocators.LK_BUTTON))

    @allure.step("Ожидам переход на страницу 'Личный кабинет'")
    def wait_for_profile_url(self):
        self.wait_for_url(Urls.LK_PROFILE_PAGE)

    @allure.step("Клик по 'История заказов'")
    def click_history_orders(self):
        self.click((By.XPATH, PersonalAccountLocators.HISTORY_ORDERS_BUTTON))

    @allure.step("Ожидание перехода на страницу 'История заказов'")
    def wait_for_history_orders_url(self):
        self.wait_for_url(Urls.HISTORY_ORDERS_PAGE)

    @allure.step("Клик по 'Выход'")
    def click_logout_button(self):
        self.click((By.XPATH, PersonalAccountLocators.LOGOUT_BUTTON))

    @allure.step("Ожидаем загрузку страницы авторизации")
    def wait_for_login_url(self):
        self.wait_for_url(Urls.LOGIN_PAGE)

