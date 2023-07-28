from uatf import *
from uatf.ui import *
from controls import *


class BasketPage(Region):
    """Страница корзины"""

    bread_crumbs = ControlBreadcrumbs()
    empty_view = Text(By.CLASS_NAME, 'cart__container', 'Корзина пуста')

    def check_load(self):
        """Проверка загрузки"""

        self.bread_crumbs.item(contains_text='Корзина').should_be(Displayed)
        self.empty_view.should_be(ContainsText('Корзина пуста'))
