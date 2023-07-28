from uatf import *
from uatf.ui import *
from controls import *


class Catalog(Region):
    """Каталог товаров"""

    bread_crumbs = ControlBreadcrumbs()
    filter = Element(By.CLASS_NAME, 'catalog-filter', 'Фильтр в каталоге')

    def check_load(self):
        """Проверяем загрузку каталога"""

        self.filter.should_be(Displayed)


