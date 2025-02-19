class FeedPageLocators:

    ORDER_HISTORY = "//li[@class='OrderHistory_listItem__2x95r mb-6']"
    WINDOW_ORDER_HISTORY = "//div[contains(@class, 'Modal_orderBox')]"
    MODAL_WINDOW_ORDER_HISTORY = "(//section[contains(@class, 'Modal_modal')])[2]"
    ORDER_CREATE_OK = "//img[@alt='tick animation']"
    ORDER_NUMBER = "//h2[contains(@class, 'Modal_modal__title__2L34m')]"
    FEED_ORDERS = "//ul[@class='OrderFeed_list__OLh59']//p[@class='text text_type_digits-default']"
    ORDER_FEED_NUMBER_ALLTIME = "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[1]"
    ORDER_FEED_NUMBER_TODAY = "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[2]"
    ORDERS_IN_WORK = "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li"
