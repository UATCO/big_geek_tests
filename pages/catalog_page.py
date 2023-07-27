from uatf import *
from uatf.ui import *


class Catalog(Region):
    """Каталог товаров"""

    bread_crumbs = CustomList(By.CLASS_NAME, 'breadcrumbs__item', 'Хлебные крошки') #вынести крошки в контрол
    filter = Element(By.CLASS_NAME, 'catalog-filter', 'Фильтр в каталоге')

    def check_load(self):
        """Проверяем загрузку каталога"""

        self.filter.should_be(Displayed)


