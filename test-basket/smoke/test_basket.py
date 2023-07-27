from uatf import *
from pages.main_page import MainPage


class TestBasket(TestCaseUI):
    """Проверяем работу корзины"""

    @classmethod
    def setUpClass(cls):
        cls.page = MainPage(cls.driver)

    def test_01_check_basket(self):
        """Проверяем открытие корзины"""

        self.page.open_basket()

    def tearDown(self):
        self.browser.close_windows_and_alert()
