from uatf import *
from uatf.ui import *


class ControlsCatalogGridAfterSearch(Control):
    """Контрол тч каталога"""

    def __str__(self):
        return 'грид каталога'

    def __init__(self, how=By.CLASS_NAME, locator='digi-products-grid', rus_name='Грид каталога', **kwargs):
        super().__init__(how, locator, rus_name, **kwargs)

        self.items = CustomList(By.CLASS_NAME,
                                'digi-product',
                                'Товары в каталоге')

        self.basket = 'digi-product-addCard'

    def add_to_basket(self, product_name: str = '', product_number: int = None):
        """Добавляем товар в корзину
        :param product_name: название товара
        :param product_number: номер товара"""

        self.item(contains_text=product_name, item_number=product_number).element(By.CLASS_NAME, self.basket).click()

    def item(self, item_number: int = 0, with_text: str = '', contains_text: str = ''):
        """Возвращает товар каталога
        :param item_number: номер товара
        :param with_text: точное совпадение текста
        :param contains_text: частичное совпадение текста"""

        return self.items.item(item_number, with_text, contains_text)

    def check_count(self, count: int):
        """Проверяем кол-во продуктов
        :param count: кол-во продуктов"""

        assert_that(lambda : self.items.count_elements, equal_to(count), 'Кол-во не совпадает', and_wait(3))

