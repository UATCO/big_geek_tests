from uatf import *
from pages.main_page import MainPage
from pages.catalog_page import Catalog


class TestFilter(TestCaseUI):
    """Проверяем работу фильтров в каталоге"""

    @classmethod
    def setUpClass(cls):
        cls.page = MainPage(cls.driver)
        cls.catalog = Catalog(cls.driver)

    def setUp(self):
        self.page.check_load()

    def test_01_check_filter_price(self):
        """Проверяем работу фильтра по цене"""

        product_name = 'Силиконовая вставка для подстаканника для Tesla Model 3 и Model Y'

        log('Переходим в каталог товаров Tesla')
        self.page.open_catalog_section('Tesla')
        self.catalog.check_load()

        log('Проверяем работу фильтра по цене')
        self.catalog.set_filter(Цена=['500', '1000'])
        self.catalog.check_count_products(1)
        card = self.catalog.open_product(product_name)
        card.check_load()
        card.check_name(product_name)

    def test_02_check_filter_brand(self):
        """Проверяем работу фильтра бренд"""

        product_name = 'Беспроводные наушники Beats Flex, серия «All-Day Wireless»'

        log('Переходим в каталог товаров Apple')
        self.page.open_catalog_section('Apple')
        self.catalog.check_load()

        log('Проверяем работу фильтра по цене')
        self.catalog.set_filter(Бренд=['Beats'])
        card = self.catalog.open_product(product_name)
        card.check_load()
        card.check_name(product_name)

    def tearDown(self):
        self.browser.close_windows_and_alert()
