from uatf import *
from pages.main_page import MainPage
from pages.catalog_page import Catalog


class TestCatalog(TestCaseUI):
    """Проверяем работу каталога"""

    @classmethod
    def setUpClass(cls):
        cls.page = MainPage(cls.driver)
        cls.catalog = Catalog(cls.driver)

    def setUp(self):
        self.page.check_load()

    def test_01_check_open_product(self):
        """Проверяем работу каталога (открытие карточки товара + сроллинг)"""

        product_name = 'Samsung Galaxy Buds'

        log('Переходим в каталог товаров Samsung')
        self.page.open_catalog_section('Samsung')
        self.catalog.check_load()

        log('Открываем карточку первого товара')
        card = self.catalog.open_product(product_name)
        card.check_name(product_name)

    def test_02_check_search(self):
        """Проверяем работу поиска"""

        log('Переходим в каталог товаров Apple')
        self.page.open_catalog_section('Apple')
        self.catalog.check_load()
        self.catalog.search_product('iphone 13')

    def tearDown(self):
        self.page.open()
        self.browser.close_windows_and_alert()
