from uatf import *
from uatf.ui import *


class OrderPage(Region):
    """Страница оформления заказа"""

    login = Button(By.CLASS_NAME, 'login-modal-singin', 'Войти')
    name = TextField(By.CSS_SELECTOR, '[name="name"]', 'Имя')
    surname = TextField(By.CSS_SELECTOR, '[name="last_name"]', 'Фамилия')
    email = TextField(By.CSS_SELECTOR, '[name="email"]', 'Электронная почта')
    phone = TextField(By.CSS_SELECTOR, '[name="phone"]', 'Мобильный телефон')
    comment = TextField(By.CSS_SELECTOR, '[name="comment"]', 'Комментарий к заказу')

    #способы получения заказа
    pickup = Button(FindBy.JQUERY, '.order-form__tab:eq(0)', 'Самовывоз')
    delivery = Button(FindBy.JQUERY, '.order-form__tab:eq(1)', 'Доставка')

    continue_btn = Button(By.CLASS_NAME, 'order-form__proceed', 'Продолжить')
    confirm_order = Button(By.CLASS_NAME, 'step-sticky__submit', 'Подтвердить заказ')
    
    def check_load(self):
        """Првоеряем загрзку страницы"""

        self.name.should_be(Displayed)

    def auth(self, email: str, password: str):
        """Авторизуемся из заказа
        :param email: логин
        :param password: пароль"""

        from pages.auth_panel import AuthPanel
        self.login.click()
        auth_panel = AuthPanel(self.driver)
        auth_panel.check_open()
        auth_panel.auth(email, password)

    def fill_order(self, **kwargs):
        """
        Заполняем поля в заказе
        Имя=''
        Фамилия=''
        Почта=''
        Телефон=''
        Комментарий=''
        """

        for key in kwargs:
            if 'Имя' == key:
                self.name.type_in(kwargs.get('Имя'))
            elif 'Фамилия' == key:
                self.surname.type_in(kwargs.get('Фамилия'))
            elif 'Почта' == key:
                self.email.type_in(kwargs.get('Почта'))
            elif 'Телефон' == key:
                self.phone.type_in(kwargs.get('Телефон'))
            elif 'Комментарий' == key:
                self.comment.type_in(kwargs.get('Комментарий'))

    def fill_ways_to_get(self, pickup: bool = True):
        """Выбираем способ получения
        :param pickup: Самовывоз - True, Доставка - False
        """

        if pickup:
            self.pickup.click()
            self.continue_btn.click()
        else:
            self.delivery.click()

    def confirm(self):
        """Подверждаем заказ"""

        self.confirm_order.click()
