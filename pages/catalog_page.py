from typing import Union

from uatf import *
from uatf.ui import *
from controls import *


class Catalog(Region):
    """Каталог товаров"""

    bread_crumbs = ControlBreadcrumbs()
    filter = Element(By.CLASS_NAME, 'catalog-filter', 'Фильтр в каталоге')
    grid = ControlCatalogGrid()

    def check_load(self):
        """Проверяем загрузку каталога"""

        self.filter.should_be(Displayed)
        self.grid.item(1).should_be(Displayed)

    def add_to_basket(self, product_name: str = '', product_number: int = None):
        """Добавляем товар корзину
        :param product_name: название товара
        :param product_number: номер товара"""

        self.grid.add_to_basket(product_name=product_name, product_number=product_number)


