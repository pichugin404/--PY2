import doctest
from typing import Union
# TODO Написать 3 класса с документацией и аннотацией типов


class Moto:

    def __init__(self, brand: str, weight: Union[int, float]):
        """
        Создание объекта Автомобиль
        :param brand: Марка мотоцикла
        :param weight: Масса мотоцикла
        :raise: TypeError: Если название марки мотоцикла не принадлежить типу str
        :raise: TypeError: Если масса мотоцикла не принадлежит типу int или float
        :raise: ValueError: Если масса мотоцикла меньше нуля
        Пример:
        >>> moto = Moto("Ural", 500)
        """
        if not isinstance(brand, str):
            raise TypeError("Название марки мотоцикла должно быть типа str")
        self.brand = brand
        if not isinstance(weight, (int, float)):
            raise TypeError("Масса мотоцикла должна быть типа int или float")
        if weight <= 0:
            raise ValueError("Масса мотоцикла должна быть строго больше нуля")
        self.weight = weight

    def moto_moving_forward(self, distance: Union[int, float]) -> None:
        """

        :param distance: Расстояние, которое нужно проехать
        :raise ValueError: Расстояние не может быть отрицательным

        Пример:
        >>> moto = Moto("Ural", 500)
        >>> moto.moto_moving_forward(10)
        """
        if distance < 0:
            raise ValueError(f"Расстояние не может быть отрицательным и не может равняться {distance}")
        ...

    def left_turn(self, angle: Union[int, float]) -> None:
        """
        :param angle: Угол поворота мотоцикла

        Пример:
        >>> moto = Moto("Ural", 500)
        >>> moto.left_turn(-30)
        """
        ...


class Bottle:
    def __init__(self, material: str, capacity: Union[int, float]):
        """
        Создание объекта Бутылка
        :param material: Материал бутылки
        :param capacity: Вместимость бутылки
        :raise: TypeError: Если название бутылки не принадлежить типу str

        Пример:
        >>> bottle = Bottle("Glass", 0.5)
        """
        if not isinstance(material, str):
            raise TypeError("Материал бутылки должно быть типа str")
        self.material = material
        if not isinstance(capacity, (int, float)):
            raise TypeError("Вместимость бутылки должна быть типа int или float")
        if capacity <= 0:
            raise ValueError("Вместимость бутылки должна быть строго больше нуля")
        self.capacity = capacity

    def pour_into_bottle(self, volume: Union[int, float]) -> None:
        """
        Наливает жидкость в бутылку
        :param volume: Объем, который нужно налить
        :raise ValueError: Объем не может быть отрицательным
        :raise TypeError: Объем должен быть либо int либо float
        Пример:
        >>> bottle = Bottle("Glass", 0.5)
        >>> bottle.pour_into_bottle(0.4)
        """
        if volume < 0:
            raise ValueError(f"Объем не может быть отрицательным и не может равняться {volume}")
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем должен быть либо int либо float")
        ...

    def break_bottle(self) -> bool:
        """
        Функция, которая проверяет, целая  бутылка или нет
        :return: Целая или нет

        Пример:
        >>> bottle = Bottle("Glass", 0.5)
        >>> bottle.break_bottle()
        """
        ...


class Terminal:
    def __init__(self, year_of_construction: int, efficiency: int):
        """
        Создание и подготовка к работе объекта Вокзал
        :param year_of_construction: год постройки
        :param efficiency: пропускная способность (млн. человек в год)
        Пример:
        >>> terminal = (2022, 40) #инициализация
        """
        if not isinstance(year_of_construction, (int)):
            raise TypeError("Год постройки должен быть типа int")
        if year_of_construction <= 0:
            raise ValueError("Год постройки должен быть больше или не равен нулю")
        self.year_of_construction = year_of_construction

        if not isinstance(efficiency, (int)):
            raise TypeError("пропускная способность должна быть типа int")
        if efficiency <= 0:
            raise TypeError("пропускная способность должна быть больше нуля")

    def train_took_off(self) -> bool:
        """
        Функция которая проверяет, выехал ли поезд или нет
        :return: выехал ли самолет
        Примеры:
        >>> terminal = Terminal(2022, 40)
        >>> terminal.train_took_off()
        """
        ...

    def come_in(self) -> bool:
        """
        Функция которая проверяет, зашли ли люди в поезд
        :return: Зашли или нет
        Примеры:
        >>> termial = Terminal(2022, 40)
        >>> termial.come_in()
        """
        ...

    def financing(self, money: Union[int, float]) -> None:
        """
        Финансирование вокзала
        :param money: количество денег, поступившее в вокзал
        :raise TypeError: money должен быть int или float
        :return: Деньги
        >>> terminal = Terminal(2022, 40)
        >>> terminal.financing(2000000)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("money должен быть int или float")

    if __name__ == "__main__":
        # TODO работоспособность экземпляров класса проверить с помощью doctest
        doctest.testmod()
