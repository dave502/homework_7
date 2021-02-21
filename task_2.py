from abc import abstractmethod, ABC


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    __V = 0

    # property size
    @property
    def v(self):
        return self.__V

    @v.setter
    def v(self, size):
        try:
            self.__V = int(size)
        except ValueError:
            print('введите пожалуйста число для утсановки размера')

    # расход ткани
    def fabric_consumption(self):
        return self.__V / 6.5 + 0.5


class Suit(Clothes):
    # height
    __H = 0

    @property
    def h(self):
        return self.__H

    @h.setter
    def h(self, height):
        try:
            self.__H = int(height)
        except ValueError:
            print('введите пожалуйста число для утсановки размера')

    def fabric_consumption(self):
        return 2 * self.__H + 0.3


# класс для оформления заказа: получение заказа и подсчет суммарного количества ткани
class Order:
    #  заказ - список объектов-дочерних классов от класса Clothes
    __clothes_total_order = []

    # расчет расхода ткани на общий заказ
    @property
    def total_fabric(self):
        # для каждого объекта-наследника Clothes из __clothes_total_order вызываем
        # функцию подсчета расхода ткани fabric_consumption() и суммируем результаты
        return sum(clothes.fabric_consumption() for clothes in list(self.__clothes_total_order)
                   if isinstance(clothes, Clothes))

    def get_order(self, clothes_class):
        """ получение заказа - какого размера какое количество
        :param clothes_class: название класса одежды, для котрого создаётся заказ
        :return:
        """
        while True:
            # запрашиваем данные
            input_data = ['size', 'quantity']
            input_order = tuple(input(f'Введите через запятую размер и количество {clothes_class.__name__}.'
                                      ' Для отмены оставьте пустую строку. ').split(','))
            # если пустая строка - выход из цикла
            if len(input_order) != 2:
                break

            # полуаем словарь для большей наглядности и удобства
            clothes_order = dict(zip(input_data, input_order))

            # добавляем объекты одежды в список общего заказа
            for i in range(int(clothes_order['quantity'])):
                # создаём объект класса, переданного в параметре функции
                obj_clothes = clothes_class()
                # задаём размер или рост (проще было бы воспользоваться консруктором, но тогда
                # не будет использоваться @setter
                if isinstance(obj_clothes, Coat):
                    obj_clothes.v = int(clothes_order['size'])
                    #print(f'Заказ на {clothes_order["quantity"]} шт. пальто с размером {obj_clothes.v} принят.')
                    # добавляем объект в общий заказ
                    self.__clothes_total_order.append(obj_clothes)

                if isinstance(obj_clothes, Suit):
                    obj_clothes.h = int(clothes_order['size'])
                    #print(f'Заказ на {clothes_order["quantity"]} шт. костюмов с ростом {obj_clothes.h} принят.')
                    # добавляем объект в общий заказ
                    self.__clothes_total_order.append(obj_clothes)


# скрипт получения заказа
order = Order()
order.get_order(Coat)
order.get_order(Suit)
print(f'Для заказанной одежды понадобится {order.total_fabric:.4}м ткани')
