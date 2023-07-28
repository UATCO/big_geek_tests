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

    def test_01_check_catalog(self):
        """Проверяем работу каталога"""

        log('Переходим в каталог товаров Samsung')
        self.page.open_catalog_section('Samsung')
        self.catalog.check_load()



    def tearDown(self):
        self.browser.close_windows_and_alert()
