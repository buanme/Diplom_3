import allure

from data import DataTest
from urls import Urls


class TestMainFunctions:

    @allure.title("Проверка, что при клике на 'Конструктор' переходим на главную страницу")
    def test_navigate_to_constructor(self, main_page):
        main_page.open()
        main_page.click_constructor()
        assert main_page.get_current_url() == Urls.MAIN_PAGE

    @allure.title("Проверка, что при клике на 'Лента заказов' переходим на страницу Лента заказов")
    def test_navigate_to_feed_orders(self, main_page, feed_page):
        main_page.open()
        main_page.click_feed_orders()
        feed_page.wait_for_url(Urls.FEED_PAGE)
        assert main_page.get_current_url() == Urls.FEED_PAGE

    @allure.title("Проверка, что при клике на ингредиент открывается окно с деталями")
    def test_modal_window_ingredients_details(self, main_page):
        main_page.open()
        main_page.click_bun()
        assert main_page.is_ingredients_details_opened()

    @allure.title("Проверка, что всплывающее окно закрывается кликом по крестику")
    def test_modal_window_closed_click_cross(self, main_page):
        main_page.open()
        main_page.click_bun()
        main_page.close_modal()
        assert not main_page.modal_is_opened()

    @allure.title("Проверка, что при добавлении ингредиента в заказ увеличивается счётчик данного ингредиента")
    def test_incremented_counter(self, main_page):
        main_page.open()
        main_page.drag_bun_to_basket()
        counter_value = main_page.get_bun_counter()
        assert counter_value == DataTest.BUNS_COUNTER

    @allure.title("Проверка, что залогиненный пользователь видит кнопку 'Оформить заказ'")
    def test_user_place_order(self, login_page, main_page):
        login_page.login(DataTest.TEST_EMAIL, DataTest.TEST_PASSWORD)
        main_page.drag_bun_to_basket()
        assert main_page.place_order_button_visible()

