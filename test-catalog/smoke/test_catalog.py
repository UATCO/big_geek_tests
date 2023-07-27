from uatf import *
from pages.main_page import MainPage


class TestCatalog(TestCaseUI):
    """Проверяем работу каталога"""

    @classmethod
    def setUpClass(cls):
        cls.page = MainPage(cls.driver)

    def test_01_check_catalog(self):
        """Проверяем работы каталога"""

        self.page.open_catalog_section('Apple')

    def tearDown(self):
        self.browser.close_windows_and_alert()
