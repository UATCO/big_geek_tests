from uatf import *
from pages.main_page import MainPage
from pages.catalog_page import Catalog


class TestBasket(TestCaseUI):
    """Проверяем работу корзины"""

    @classmethod
    def setUpClass(cls):
        cls.page = MainPage(cls.driver)
        cls.catalog = Catalog(cls.driver)

    def test_01_add_to_basket_from_catalog(self):
        """Проверяем добавление/удаление товара из каталога"""

        product_name = 'Samsung Galaxy Buds'

        log('Переходим в каталог товаров Samsung')
        self.page.open_catalog_section('Samsung')
        self.catalog.check_load()

        log('Добавляем товар в корзину')
        card_mini = self.catalog.add_to_basket(product_name)
        basket_page = card_mini.go_to_basket()
        basket_page.check_product_exist(product_name)

        log('Удаляем товар из корзины')
        basket_page.delete_product(product_name)
        basket_page.check_product_exist(product_name, displayed=False)

    def test_02_add_to_basket_from_card(self):
        """Проверяем добавление товара из карточки товара"""

        product_name = 'Samsung Galaxy Buds'

        log('Переходим в каталог товаров Samsung')
        self.page.open_catalog_section('Samsung')
        self.catalog.check_load()
        card = self.catalog.open_product(product_name)

        log('Проверяем добавление товара в корзину из карточки')
        card_mini = card.add_to_basket()
        basket = card_mini.go_to_basket()
        basket.check_product_exist(product_name)

    def tearDown(self):
        self.page.open()
        self.browser.close_windows_and_alert()
