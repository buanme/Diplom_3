import allure

from data import DataTest
from urls import Urls


class TestRestorePassword:

    @allure.title("Проверка, что переход на страницу восстановления пароля по кнопке 'Восстановить пароль' работает")
    def test_navigate_to_page_restore_password_with_button(self, login_page):
        login_page.open()
        login_page.click_forgot_password()
        assert login_page.get_current_url() == Urls.FORGOT_PASSWORD_PAGE

    @allure.title("Проверка ввода почты и клика по кнопке 'Восстановить'")
    def test_restore_button(self, restore_password_page):
        restore_password_page.open()
        restore_password_page.fill_email(DataTest.TEST_EMAIL)
        restore_password_page.click_restore_button()
        restore_password_page.wait_for_reset_password_url()
        assert restore_password_page.get_current_url() == Urls.RESET_PASSWORD_PAGE

    @allure.title("Проверка, что клик по кнопке показать/скрыть пароль активирует поле (подсвечивает)")
    def test_show_hide_password_button(self, restore_password_page):
        restore_password_page.open()
        restore_password_page.fill_email(DataTest.TEST_EMAIL)
        restore_password_page.click_restore_button()
        restore_password_page.click_show_hide_button()
        input_class = restore_password_page.get_input_status()
        placeholder_class = restore_password_page.get_placeholder_status()
        assert DataTest.INPUT_STATUS_ACTIV in input_class and DataTest.INPUT_PLACEHOLDER in placeholder_class
