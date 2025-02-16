import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @allure.step("Открыть страницу")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Ждем видимость элемента")
    def wait_to_visibility(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ждем кликабельность элемента")
    def wait_to_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Клик")
    def click(self, locator):
        self.wait_to_clickable(locator)
        self.driver.find_element(*locator).click()

    @allure.step("Заполняем поле")
    def fill(self, locator, text):
        self.wait_to_visibility(locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получаем текст")
    def get_text(self, locator):
        self.wait_to_visibility(locator)
        return self.driver.find_element(*locator).text

    @allure.step("Ждем переход на страницу")
    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @allure.step("Перетаскиваем элемент")
    def drag_and_drop(self, source_locator, target_locator):
        self.wait_to_clickable(source_locator)
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
