class MainPageLocators:
    CONSTRUCTOR_BUTTON = "//p[text()='Конструктор']"
    FEED_ORDERS_BUTTON = "//p[text()='Лента Заказов']"

    BUN_R2_D3 = "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]"
    BUN_R2_D3_COUNTER = "//p[contains(text(), 'R2-D3')]/preceding-sibling::div[contains(@class, 'counter_counter')]//p"
    BUN_R2_D3_DETAILS = "//p[contains(text(), 'Флюоресцентная булка R2-D3')]"

    MODAL_WINDOW_INGREDIENTS_DETAILS = "//div[@class='Modal_modal__container__Wo2l_']"
    INGREDIENTS_DETAILS = "//h2[contains(text(), 'Детали ингредиента')]"
    CLOSE_BUTTON = "//button[contains(@class, 'close_modified')]"
    MODAL_WINDOW = "(//section[contains(@class, 'Modal_modal')])[1]"

    BASKET = "//ul[@class='BurgerConstructor_basket__list__l9dp_']"
    PLACE_ORDER_BUTTON = "//button[text()='Оформить заказ']"
