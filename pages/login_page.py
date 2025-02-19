from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from urls import Urls


class LoginPage(BasePage):

    @allure.step("Открываем страницу авторизации")
    def open(self):
        self.open_url(Urls.LOGIN_PAGE)

    @allure.step("Заполняем эмейл")
    def set_email(self, email):
        self.fill((By.XPATH, LoginLocators.LOGIN_NAME_INPUT), email)

    @allure.step("Заполняем пароль")
    def set_password(self, password):
        self.fill((By.XPATH, LoginLocators.LOGIN_PASSWORD_INPUT), password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_submit(self):
        self.click((By.XPATH, LoginLocators.LOGIN_SUBMIT_BUTTON))

    @allure.step("Клик по кнопке 'Восстановить пароль'")
    def click_forgot_password(self):
        self.click((By.XPATH, LoginLocators.FORGOT_PASSWORD_BUTTON))

    @allure.step("Авторизация")
    def login(self, email, password):
        self.open()
        self.set_email(email)
        self.set_password(password)
        self.click_submit()
