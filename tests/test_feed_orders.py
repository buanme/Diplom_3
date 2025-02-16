import allure

from auth import Auth


class TestFeedOrders:

    @allure.title("Проверка, что при клике на заказ открывается всплывающее окно с деталями")
    def test_modal_window_details_order(self, feed_page):
        feed_page.open()
        feed_page.open_order_detail_modal()
        assert feed_page.modal_is_opened()

    @allure.title("Проверка, что созданный пользователем заказ отображается на странице Лента заказов")
    def test_displaying_user_orders(self, login_page, main_page, feed_page):
        login_page.login(Auth.EMAIL, Auth.PASSWORD)
        main_page.drag_bun_to_basket()
        order_number = feed_page.create_order_and_get_number()
        feed_page.open()
        assert feed_page.is_order_in_feed(order_number)

    @allure.title("Проверка, что при создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_counter_alltime(self, main_page, feed_page, login_page):
        feed_page.open()
        old_value = feed_page.get_alltime_counter()
        login_page.login(Auth.EMAIL, Auth.PASSWORD)
        main_page.drag_bun_to_basket()
        feed_page.create_order_and_get_number()
        feed_page.open()
        new_value = feed_page.get_alltime_counter()
        assert int(new_value) > int(old_value)

    @allure.title("Проверка, что при создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_counter_today(self, main_page, feed_page, login_page):
        feed_page.open()
        old_value = feed_page.get_today_counter()
        login_page.login(Auth.EMAIL, Auth.PASSWORD)
        main_page.drag_bun_to_basket()
        feed_page.create_order_and_get_number()
        feed_page.open()
        new_value = feed_page.get_today_counter()
        assert int(new_value) > int(old_value)

    @allure.title("Проверка, что номер оформленного заказа появляется в разделе 'В работе'")
    def test_order_in_work(self, main_page, feed_page, login_page):
        login_page.login(Auth.EMAIL, Auth.PASSWORD)
        main_page.drag_bun_to_basket()
        order_number = feed_page.create_order_and_get_number()
        feed_page.open()
        feed_page.wait_for_order_in_work(order_number)
        assert feed_page.is_order_in_work(order_number)

