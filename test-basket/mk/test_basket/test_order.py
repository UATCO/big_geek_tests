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
        """Проверяем оформление заказа"""

        product_name = 'Samsung Galaxy Buds'

        log('Переходим в каталог товаров Apple')
        self.page.open_catalog_section('Apple')
        self.catalog.check_load()

        log('Добавляем товар в корзину')
        card_mini = self.catalog.add_to_basket(product_number=1)
        basket_page = card_mini.go_to_basket()