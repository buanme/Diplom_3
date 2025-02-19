from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from locators.restore_password_locators import RestorePasswordLocators
from urls import Urls


class RestorePasswordPage(BasePage):

    @allure.step("Открытие старницы Восстановления пароля")
    def open(self):
        self.open_url(Urls.FORGOT_PASSWORD_PAGE)

    @allure.step("Заполнение эмейла")
    def fill_email(self, email):
        self.send_keys((By.NAME, RestorePasswordLocators.INPUT_EMAIL), email)

    @allure.step("Нажать на кнопку 'Восстановить'")
    def click_restore_button(self):
        self.click((By.XPATH, RestorePasswordLocators.RESTORE_BUTTON))

    @allure.step("Клик по глазику")
    def click_show_hide_button(self):
        self.click((By.XPATH, RestorePasswordLocators.SHOW_HIDE_BUTTON))

    @allure.step("Проверка видимости пароля")
    def get_input_status(self):
        return self.get_class_by_locator((By.XPATH, RestorePasswordLocators.INPUT_STATUS_ACTIVE))

    @allure.step("Проверка фокуса")
    def get_placeholder_status(self):
        return self.get_class_by_locator((By.XPATH, RestorePasswordLocators.PLACEHOLDER_FOCUSED))

    @allure.step("Переход на страницу Восстановления пароля")
    def wait_for_reset_password_url(self):
        self.wait_for_url(Urls.RESET_PASSWORD_PAGE)

