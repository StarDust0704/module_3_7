# module_3_7

def calculate_structure_sum(data):
    total_sum = 0

    # Рекурсивная функция для суммирования значений
    def process_data(item):
        nonlocal total_sum

        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, dict):
            for key in item:
                process_data(key)
                process_data(item[key])
        elif isinstance(item, list) or isinstance(item, tuple):
            for value in item:
                process_data(value)

    # Обработка входных данных
    process_data(data)

    return total_sum


# Входные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

# Вызов функции
result = calculate_structure_sum(data_structure)

# Вывод результата
print(result)





