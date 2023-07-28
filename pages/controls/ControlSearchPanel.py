from uatf import *
from uatf.ui import *


class ControlSearchPanel(Control):
    """Панель поиска"""

    def __str__(self):
        return "панель поиска"

    def __init__(self, how=By.CLASS_NAME, locator='digi-ac', rus_name='Панель поиска'):
        super().__init__(how, locator, rus_name)

        self.history_panel = Element(By.CLASS_NAME,
                                     'digi-ac__set_main',
                                     'История поиска')

        self.product_panel = Element(By.CLASS_NAME,
                                     'digi-ac__set_products',
                                     'Продукты')

    def check_open(self):
        """Проверяем открытие панели"""

        self.product_panel.should_be(Displayed)
