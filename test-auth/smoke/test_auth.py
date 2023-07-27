from uatf import *
from pages.main_page import MainPage


class TestAuth(TestCaseUI):
    """Проверяем работу авторизации"""

    @classmethod
    def setUpClass(cls):
        cls.page = MainPage(cls.driver)

    def test_01_check_auth(self):
        """Проверяем авторизацию из главной страницы"""

        self.page.auth(self.config.CUSTOM.get('USER_NAME'), self.config.CUSTOM.get('PASSWORD'))

    def tearDown(self):
        self.browser.close_windows_and_alert()
