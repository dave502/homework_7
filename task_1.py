
class Matrix:
    __matrix = []

    # size - размероность матрицы - количество списков в списке
    @property
    def size(self):
        return len(self.__matrix)

    #  в конструкторе проверяем правильность матрицы
    def __init__(self, matrix_list: list):
        #  если передана некорректная матрица - завершаем скрипт
        if not self.__check_matrix(matrix_list):
            print('Передан некорректный формат матрицы')
            raise SystemExit
        #  иначе - сохраняем в атрибут класса
        else:
            self.__matrix = matrix_list

    # __str__- каждый list матрицы записываем в отдельную строку и возвращаем полученный текст
    def __str__(self):
        print_matrix = '\n'
        for str_matrix in self.__matrix:
            print_matrix += ''.join(f'{i:5}' for i in str_matrix) + '\n'
        return print_matrix

    # поочерёдно суммируем все списки матриц, если матрицы разной длины - выбираем меньшую размерность
    def __add__(self, other):
        sum_matrix = []
        matrix_size = self.size

        # сравниваем размерность суммируемых матриц, если размерность разная - выбираем меньшую
        if matrix_size != other.size:
            print('Нельзя суммировать матрицы разной размерности. '
                  'Часть матрицы с большей размерностью будет отсечена.')
            matrix_size = other.size if other.size < matrix_size else matrix_size

        for i in range(matrix_size):
            sum_matrix.append(list(map(lambda x, y: x + y, self[i], other[i])))

        return Matrix(sum_matrix)

    # получаем строку матрицы по номеру
    def __getitem__(self, i):
        return self.__matrix[i]

    # проверка переданной в конструктор матрицы на соответствие основным условиям
    def __check_matrix(self, matrix_to_check):
        right_matrix = False
        # проверка,что тип переданного параметра list
        if isinstance(matrix_to_check, list):
            # сравнение, что все вложенные списки одного размера
            size_list = len(matrix_to_check[1])
            for el_list in matrix_to_check:
                # проверка,что элементы списка также являются списками
                if isinstance(el_list, list) and len(el_list) == size_list:
                    # проверка,что элементы каждого списка являются числами
                    try:
                        list(map(lambda x: sum(x), matrix_to_check))
                        # все условия выполнены
                        right_matrix = True
                    except:
                        print('Матрица содержит некорректные символы')
                        right_matrix = False
                        break
                else:
                    break
        return right_matrix


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
matrix_other = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]])

print(f'результат сложения матриц {matrix} и {matrix_other} = {matrix + matrix_other}')

