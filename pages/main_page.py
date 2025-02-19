from selenium.webdriver.common.by import By
import allure

from data import DataTest
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open(self):
        self.open_url(Urls.MAIN_PAGE)

    @allure.step("Клик по 'Конструктор'")
    def click_constructor(self):
        self.click((By.XPATH, MainPageLocators.CONSTRUCTOR_BUTTON))

    @allure.step("Клик по 'Лента заказов'")
    def click_feed_orders(self):
        self.click((By.XPATH, MainPageLocators.FEED_ORDERS_BUTTON))

    @allure.step("Клик по булке R2-D3")
    def click_bun(self):
        self.click((By.XPATH, MainPageLocators.BUN_R2_D3))

    @allure.step("Проверка модального окна ингедиента")
    def is_ingredients_details_opened(self):
        title_text = self.get_text((By.XPATH, MainPageLocators.INGREDIENTS_DETAILS))
        bun_name = self.get_text((By.XPATH, MainPageLocators.BUN_R2_D3_DETAILS))
        return title_text == DataTest.INGREDIENTS_DETAILS_TEXT and DataTest.BUN_NAME in bun_name

    @allure.step("Закрытие модального окна ингедиента")
    def close_modal(self):
        self.click((By.XPATH, MainPageLocators.CLOSE_BUTTON))

    @allure.step("Проверка открытия модального окна")
    def modal_is_opened(self):
        modal_class = self.get_class_by_locator((By.XPATH, MainPageLocators.MODAL_WINDOW))
        return DataTest.MODAL_OPENED in modal_class

    @allure.step("Добавление булки R2-D3 в корзину")
    def drag_bun_to_basket(self):
        self.drag_and_drop((By.XPATH, MainPageLocators.BUN_R2_D3), (By.XPATH, MainPageLocators.BASKET))

    @allure.step("Получение количества булок R2-D3")
    def get_bun_counter(self):
        return self.get_text((By.XPATH, MainPageLocators.BUN_R2_D3_COUNTER))

    @allure.step("Проверка наличия кнопки 'Оформить заказ'")
    def place_order_button_visible(self):
        return self.get_text_by_locator((By.XPATH, MainPageLocators.PLACE_ORDER_BUTTON)) == DataTest.PLACE_ORDER
