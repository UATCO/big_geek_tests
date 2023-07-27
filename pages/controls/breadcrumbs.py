from uatf import *
from uatf.ui import *


class Breadcrumbs(Control):
    """Хлебные крошки"""

    def __str__(self):
        return "хлебные крошки"

    def __init__(self, how=By.CLASS_NAME, locator='breadcrumbs__item', rus_name='Хлебные крошки'):
        super().__init__(how, locator, rus_name)

        self.breadcrumbs = CustomList(By.CLASS_NAME,
                                      'breadcrumbs__item',
                                      'Хлебные крошки')

    def back(self):
        """Возвращаемся на один пункт назад"""

        last_crumb = self.breadcrumbs.count_elements
        log('Возвращаемся на один пункт назад через хлебные крошки')
        self.item(item_number=last_crumb).click()

    def go_to_crumb(self, crumb: str):
        """Кликаем по необходимой крошке
        :param crumb: название крошки"""

        self.item(contains_text=crumb).click()

    def item(self, item_number: int = 0, with_text: str = '', contains_text: str = ''):
        """Возвращает хлебную крошку
        :param item_number: номер крошки
        :param with_text: точное совпадение текста
        :param contains_text: частичное совпадение текста"""

        return self.breadcrumbs.item(item_number, with_text, contains_text)