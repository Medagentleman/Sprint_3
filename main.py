import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        """Конструктор класса - инициализирует все атрибуты"""
        # Приватные атрибуты (начинаются с __) - защищены от прямого доступа
        self.__name_items = []  # список товаров в текущем чеке
        self.__number_items = 0  # количество товаров в чеке
        # Справочник цен на товары (не меняется)
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45,
                             'молоко': 55, 'кефир': 70}
        # Справочник налоговых ставок (не меняется)
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20,
                           'молоко': 10, 'кефир': 10}

    # 1. ГЕТТЕРЫ
    @property
    def name_items(self):
        """Геттер для списка товаров"""
        return self.__name_items

    @property
    def number_items(self):
        """Геттер для количества товаров"""
        return self.__number_items

    # 2. ДОБАВЛЕНИЕ ТОВАРА В ЧЕК
    def add_item_to_cheque(self, name):

        # Проверка 1: длина названия от 1 до 40 символов
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')

        # Проверка 2: есть ли товар в справочнике цен
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')

        # Если все проверки пройдены - добавляем товар
        self.__name_items.append(name)
        self.__number_items += 1

    # 3. УДАЛЕНИЕ ТОВАРА ИЗ ЧЕКА
    def delete_item_from_check(self, name):

        # Проверяем, есть ли товар в чеке
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')

        # Удаляем одно вхождение товара (первое попавшееся)
        self.__name_items.remove(name)
        self.__number_items -= 1

    # 4. РАСЧЕТ ОБЩЕЙ СТОИМОСТИ
    def check_amount(self):

        total = []  # список для цен товаров

        # Проходим по всем товарам в чеке
        for item in self.__name_items:
            # Берем цену из справочника и добавляем в список
            total.append(self.__item_price[item])

        # Считаем сумму всех цен
        sum_total = sum(total)

        # Если товаров больше 10 - применяем скидку 10%
        if self.__number_items > 10:
            return sum_total * 0.9  # сумма со скидкой
        else:
            return sum_total  # полная сумма

    # 5. НДС ДЛЯ ТОВАРОВ СО СТАВКОЙ 20%
    def twenty_percent_tax_calculation(self):
        """
        Считает НДС 20% для товаров с соответствующей ставкой
        """
        twenty_percent_tax = []  # список товаров со ставкой 20%
        total = []  # список их цен

        # Проходим по товарам в чеке
        for item in self.__name_items:
            # Если ставка налога 20% - добавляем в список
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])

        # Считаем общую стоимость этих товаров
        sum_total = sum(total)

        # Применяем скидку если нужно
        if self.__number_items > 10:
            sum_total = sum_total * 0.9

        # НДС = стоимость * 0.2 (20%)
        return sum_total * 0.2

    # 6. НДС ДЛЯ ТОВАРОВ СО СТАВКОЙ 10%
    def ten_percent_tax_calculation(self):
        """
        Считает НДС 10% для товаров с соответствующей ставкой
        """
        ten_percent_tax = []  # список товаров со ставкой 10%
        total = []  # список их цен

        # Проходим по товарам в чеке
        for item in self.__name_items:
            # Если ставка налога 10% - добавляем в список
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])

        # Считаем общую стоимость этих товаров
        sum_total = sum(total)

        # Применяем скидку если нужно
        if self.__number_items > 10:
            sum_total = sum_total * 0.9

        # НДС = стоимость * 0.1 (10%)
        return sum_total * 0.1

    # 7. ОБЩАЯ СУММА НАЛОГОВ ПО ЧЕКУ
    def total_tax(self):
        """
        Возвращает общую сумму НДС по чеку
        """
        # Просто складываем результаты двух предыдущих методов
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    # 8. ФОРМАТИРОВАНИЕ НОМЕРА ТЕЛЕФОНА (статический метод)
    @staticmethod
    def get_telephone_number(telephone_number):
        """
        Статический метод - не зависит от экземпляра класса
        Форматирует номер телефона: +7 и 10 цифр
        """
        # Проверка типа: должно быть целое число
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')

        # Преобразуем в строку для проверки длины
        tel_str = str(telephone_number)

        # Проверка длины: должно быть ровно 10 цифр
        if len(tel_str) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        # Возвращаем отформатированный номер
        return f'+7{tel_str}'


# Проверки работы
if __name__ == "__main__":
    # Создаем экземпляр кассы
    cash_register = OnlineSalesRegisterCollector()

    print("=== ТЕСТИРОВАНИЕ РАБОТЫ КАССЫ ===\n")

    # 1. Добавляем товары
    print("1. Добавляем товары в чек:")
    cash_register.add_item_to_cheque('чипсы')
    cash_register.add_item_to_cheque('молоко')
    cash_register.add_item_to_cheque('кола')
    cash_register.add_item_to_cheque('печенье')
    cash_register.add_item_to_cheque('кефир')
    print(f"   Товары в чеке: {cash_register.name_items}")
    print(f"   Количество товаров: {cash_register.number_items}\n")

    # 2. Проверяем геттеры
    print("2. Проверка геттеров:")
    print(f" name_items: {cash_register.name_items}")
    print(f" number_items: {cash_register.number_items}\n")

    # 3. Считаем общую сумму
    print("3. Расчет общей суммы:")
    print(f"   Сумма чека: {cash_register.check_amount()} руб.\n")

    # 4. Считаем налоги
    print("4. Расчет налогов:")
    print(f"   НДС 20%: {cash_register.twenty_percent_tax_calculation()} руб.")
    print(f"   НДС 10%: {cash_register.ten_percent_tax_calculation()} руб.")
    print(f"   Общий НДС: {cash_register.total_tax()} руб.\n")

    # 5. Удаляем товар
    print("5. Удаление товара:")
    cash_register.delete_item_from_check('кола')
    print(f"   После удаления 'кола': {cash_register.name_items}")
    print(f"   Количество товаров: {cash_register.number_items}\n")

    # 6. Форматирование телефона
    print("6. Форматирование телефона:")
    phone = OnlineSalesRegisterCollector.get_telephone_number(1234567890)
    print(f"   Телефон: {phone}\n")

    # 7. Тестирование исключений
    print("7. Тестирование исключений (будут ошибки):")
    try:
        cash_register.add_item_to_cheque('')  # пустое название
    except ValueError as e:
        print(f"   Ошибка при пустом названии: {e}")

    try:
        cash_register.add_item_to_cheque('хлеб')  # товара нет в справочнике
    except NameError as e:
        print(f"   Ошибка при отсутствующем товаре: {e}")

    try:
        OnlineSalesRegisterCollector.get_telephone_number(123)  # мало цифр
    except ValueError as e:
        print(f"   Ошибка в номере телефона: {e}")