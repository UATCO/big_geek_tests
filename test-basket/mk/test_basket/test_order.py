from uatf import *
from pages.main_page import MainPage
from pages.catalog_page import Catalog


class TestOrder(TestCaseUI):
    """Проверяем оформление заказа"""

    @classmethod
    def setUpClass(cls):
        cls.page = MainPage(cls.driver)
        cls.catalog = Catalog(cls.driver)

    def test_01_make_order(self):
        """Проверяем оформление заказа c самовывозом"""

        log('Переходим в каталог товаров Apple')
        self.page.open_catalog_section('Apple')
        self.catalog.check_load()

        log('Добавляем товар в корзину')
        card_mini = self.catalog.add_to_basket(product_number=1)
        basket_page = card_mini.go_to_basket()

        log('Оформляем заказ')
        order = basket_page.make_order()
        order.auth(self.config.CUSTOM.get('USER_NAME'), self.config.CUSTOM.get('PASSWORD'))
        order.fill_order(Имя='Тест', Фамилия='Тестовый', Почта='testovyy1999@inbox.ru', Телефон='89196920906',
                         Комментарий='Тест, заказ можно отменить')
        order.fill_ways_to_get()
        order.confirm()

