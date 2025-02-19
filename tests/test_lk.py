import allure

from data import DataTest
from urls import Urls


class TestLK:

    @allure.title("Проверка перехода по клику на 'Личный кабинет' после авторизации")
    def test_navigate_to_lk(self, login_page, personal_account_page):
        login_page.login(DataTest.TEST_EMAIL, DataTest.TEST_PASSWORD)
        personal_account_page.click_lk_button()
        personal_account_page.wait_for_profile_url()
        assert personal_account_page.get_current_url() == Urls.LK_PROFILE_PAGE

    @allure.title("Проверка перехода в раздел 'История заказов'")
    def test_navigate_to_history_orders(self, login_page, personal_account_page):
        login_page.login(DataTest.TEST_EMAIL, DataTest.TEST_PASSWORD)
        personal_account_page.click_lk_button()
        personal_account_page.wait_for_profile_url()
        personal_account_page.click_history_orders()
        personal_account_page.wait_for_history_orders_url()
        assert personal_account_page.get_current_url() == Urls.HISTORY_ORDERS_PAGE

    @allure.title("Проверка, что по клику Выход производится логаут и переходим на страницу логина")
    def test_logout_from_lk(self, login_page, personal_account_page):
        login_page.login(DataTest.TEST_EMAIL, DataTest.TEST_PASSWORD)
        personal_account_page.click_lk_button()
        personal_account_page.wait_for_profile_url()
        personal_account_page.click_logout_button()
        personal_account_page.wait_for_login_url()
        assert personal_account_page.get_current_url() == Urls.LOGIN_PAGE
