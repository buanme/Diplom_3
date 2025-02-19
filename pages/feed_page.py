from selenium.webdriver.common.by import By
import allure

from data import DataTest
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from urls import Urls


class FeedPage(BasePage):

    @allure.step("Открываем страницу Лента заказов")
    def open(self):
        self.open_url(Urls.FEED_PAGE)

    @allure.step("Кликаем по последнему созданному заказу")
    def open_order_detail_modal(self):
        self.wait_to_visibility((By.XPATH, FeedPageLocators.ORDER_HISTORY))
        self.click((By.XPATH, FeedPageLocators.ORDER_HISTORY))

    @allure.step("Проверка открытия модального окна")
    def modal_is_opened(self):
        self.wait_to_visibility((By.XPATH, FeedPageLocators.WINDOW_ORDER_HISTORY))
        modal_class = self.get_class_by_locator((By.XPATH, FeedPageLocators.MODAL_WINDOW_ORDER_HISTORY))
        return DataTest.MODAL_OPENED in modal_class

    @allure.step("Создаем заказ")
    def create_order_and_get_number(self):
        self.click((By.XPATH, MainPageLocators.PLACE_ORDER_BUTTON))
        self.wait_to_visibility((By.XPATH, FeedPageLocators.ORDER_CREATE_OK))
        self.wait_until(lambda d: d.find_element(By.XPATH, FeedPageLocators.ORDER_NUMBER).text != DataTest.NUMBER_PLACEHOLDER)
        order_number = self.get_text((By.XPATH, FeedPageLocators.ORDER_NUMBER))
        return f"#{int(order_number):07d}"  # переводим в формат #0000000

    @allure.step("Проверяем наличие заказа в списке заказов")
    def is_order_in_feed(self, order_number):
        self.wait_to_visibility((By.XPATH, FeedPageLocators.FEED_ORDERS))
        orders_elements = self.find_elements((By.XPATH, FeedPageLocators.FEED_ORDERS))
        return any(el.text in order_number for el in orders_elements)

    @allure.step("Счетчик 'Выполнено за все время'")
    def get_alltime_counter(self):
        return self.get_text((By.XPATH, FeedPageLocators.ORDER_FEED_NUMBER_ALLTIME))

    @allure.step("Счетчик 'Выполнено за сегодня'")
    def get_today_counter(self):
        return self.get_text((By.XPATH, FeedPageLocators.ORDER_FEED_NUMBER_TODAY))

    @allure.step("Проверяем наличие заказа 'В работе'")
    def is_order_in_work(self, order_number):
        return any(el.text in order_number for el in self.find_elements((By.XPATH, FeedPageLocators.ORDERS_IN_WORK)))

    @allure.step("Ждем наличие заказа 'В работе'")
    def wait_for_order_in_work(self, order_number):
        self.wait_until(lambda d: any(el.text in order_number for el in d.find_elements(By.XPATH, FeedPageLocators.ORDERS_IN_WORK)))
