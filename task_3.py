from math import floor


class Cell:
    __cells_count = 0

    def __init__(self, count, iter_start=0):
        self.__cells_count = count
        self.i = iter_start

    # создаётся новая клетка с количеством, равным сумме двух слагаемых
    def __add__(self, added_cell):
        if isinstance(added_cell, Cell):
            return Cell(self.__cells_count + added_cell.cells_count)

    # из количества первой клетки вычитается количество второй, возращается этот объект
    def __sub__(self, subducted_cell):
        if isinstance(subducted_cell, Cell):
            dif = self.__cells_count - subducted_cell.cells_count
            if dif > 0:
                self.__cells_count = dif
            else:
                print('Разность количества ячеек двух клеток меньше нуля')
        return self

    # создаётся новая клетка с количеством, равным произведению двух множителей
    def __mul__(self, multed_cell):
        if isinstance(multed_cell, Cell):
            return Cell(self.__cells_count * multed_cell.cells_count)

    # создаётся новая клетка с количеством, равным делению количества этого объекта на другой
    def __truediv__(self, other_cell):
        if isinstance(other_cell, Cell):
            # округление в меньшую сторону
            result = floor(self.__cells_count / other_cell.cells_count)
            return Cell(result)

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= self.__cells_count:
            return self.i
        else:
            self.i = 0
            raise StopIteration

    def __str__(self):
        return f'Объект класса Cell с количеством клеток = {self.__cells_count}'

    @property
    def cells_count(self):
        return self.__cells_count

    #  в учебных целях добавим интерфейс итерации и
    #  выведем с его помощью клетки в ряды
    @staticmethod
    def make_order(cell, cells_in_row):
        if isinstance(cell, Cell):
            for i, one_cell in enumerate(cell, start=1):
                print('*' + ('\n' if not (i % cells_in_row) else ''), end='')
            print('\n')


cell1 = Cell(25)
cell2 = Cell(10)

print(f'cell1 + cell2 = {cell1 + cell2}')  # Объект класса Cell с количеством клеток = 35
print(f'cell1 - cell2 = {cell1 - cell2}')  # Объект класса Cell с количеством клеток = 15
print(f'cell2 - cell1 = {cell2 - cell1}')  # Разность количества ячеек двух клеток меньше нуля
# Объект класса Cell с количеством клеток = 10
print(f'cell2 * cell1 = {cell2 * cell1}')  # Объект класса Cell с количеством клеток = 150
print(f'cell2 / cell1 = {cell1 / cell2}')  # Объект класса Cell с количеством клеток = 1

Cell.make_order(cell1, 4)
Cell.make_order(cell2, 5)
