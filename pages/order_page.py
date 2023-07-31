from uatf import *
from uatf.ui import *


class OrderPage(TestCaseUI):
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
    
