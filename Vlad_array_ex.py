def array_diagonal_sums(array):

    sum_diag_first = 0
    sum_diag_second = 0
    array_dimension = len(array)

    for i in range(array_dimension):
        sum_diag_first = sum_diag_first + array[i][i]                           # Сумма по диагонали 1
        sum_diag_second = sum_diag_second + array[i][array_dimension - 1 - i]   # Сумма по диагонали 2

    return [array_dimension, sum_diag_first, sum_diag_second]


def create_array(dimension_columns_rows):
    array = []
    rows = dimension_columns_rows[1]
    columns = dimension_columns_rows[0]

    for i in range(rows):
        row = []
        for x in range(columns):
            row.append(' ')
        array.append(row)

    return array


def fill_letter_in_array(array, letter_for_array):
    for i in range(len(array)):
        for x in letter_for_array[i]:
            array[i][x] = "B"

    return array


def print_array(array):
    # вывод как массива
    for i in array:
        print(i)
    # вывод как буквы "попиксельно"
    for i in array:
        for x in i:
            print(x, end='')
        print(end='\n')


def main():
    # входящие данные (массив) для подсчета суммы по диагоналям
    array_test_for_sum = [
                          [22, 10, 12],
                          [0, -4, 17],
                          [44, 99, 14]
                         ]

    # входящие данные для буквы в массиве: размерность массива с пробелами и схема буквы "попиксельно"
    # (указаны индексы элементов массива, в которых пробел будет заменен на печатный символ
    array_dimension_for_letter = [7, 10]
    letter_for_array = [
                        [0, 1, 2],
                        [0, 3],
                        [0, 4],
                        [0, 3],
                        [0, 1, 2],
                        [0, 3, 4],
                        [0, 5],
                        [0, 6],
                        [0, 5],
                        [0, 1, 2, 3, 4]
                       ]

# расчет суммы диагоналей для квадратного массива
    result_diagonal_sums = array_diagonal_sums(array_test_for_sum)
    print(
         'Размерность квадратного массива: ', result_diagonal_sums[0], '\n',
         'Сумма первой диагонали: ', result_diagonal_sums[1], '\n',
         'Сумма второй диагонали: ', result_diagonal_sums[2]
         )

# создание массива и заполнение данными по узору (букве)
    empty_array = create_array(array_dimension_for_letter)
    array_with_letter = fill_letter_in_array(empty_array, letter_for_array)
    print_array(array_with_letter)


if __name__ == '__main__':
    main()


# тут недописанная функция по определению минимальной размерности массива
# для функции подсчета суммы диагоналей массива
# (массив должен быть квадратным, т.е. количество столбцов == количество строк)
#
# def min_array_dimension(array):
#
#     # min of rows
#     rows = min(len([array[i] for i in range(len(array))]))
#     print(rows)
#
#     # #min_of_rows = min(len(array[i] for i in range(len(array)-1)))
#     # print('min_of_rows: ', min_of_rows)
#     #
#     # min_dimension = min_of_rows
#
#     return #min_dimension
#
#     # if len(array_test) == all((array_test[i] for i in range(len(array_test)))):
#     #     array_dimension = len(array_test)
#     # else:
#     #     print('Массив НЕ квадратный')
#     #     array_dimension = min(len(array_test), min(array_test[i] for i in range(len(array_test))))
