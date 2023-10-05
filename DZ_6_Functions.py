# Завдання 1
#
# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

# def calculate_product(numbers):
#     product = 1
#
#     for num in numbers:
#         product *= num
#
#     return product
#
# my_list = [n for n in range(2, 7)]
# print(my_list)
# product = calculate_product(my_list)
# print(product)


# Завдання 2
#
# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

import random


def get_list_of_numbers(list_length=10, start=1, end=7):
    numbers = []

    for _ in range(list_length):
        numbers.append(random.randint(start, end))
    return numbers


my_list = get_list_of_numbers()
print(my_list)


# def find_min_number(numbers) -> list:
#     min_number = numbers[0]
#
#     for i in numbers:
#         if i < min_number:
#             min_number = i
#
#     return min_number
#
# min_number = find_min_number(my_list)
# print(min_number)


# Завдання 3
#
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.


# def find_simple_number(i):
#     if i <= 1:
#         return False
#     if i <= 3:
#         return True
#     if i % 2 == 0 or i % 3 == 0:
#         return False
#
#     a = 5
#     while a * a <= i:
#         if i % a == 0 or i % (a + 2) == 0:
#             return False
#         i += 6
#     return True
#
#
# def simple_num_count(list_1):
#     quantity = 0
#     for i in list_1:
#         if find_simple_number(i):
#             quantity += 1
#     return quantity
#
#
# quantity_simple = simple_num_count(my_list)
# simple_number_list = find_simple_number
# print(simple_number_list)
# print(quantity_simple)


# Завдання 4
#
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

# def remove_number(numbers, number):
#
#     deleted_quantity = numbers.count(number)
#
#     for _ in range(deleted_quantity):
#         numbers.remove(number)
#
#     return deleted_quantity
#
#
# number_for_removal = 3
# deleted_quantity = remove_number(my_list, number_for_removal)
# print(deleted_quantity)
# print(my_list)


# Завдання 5
#
# Напишіть функцію, яка отримує два списки як параметр і повертає список,
# що містить елементи обох списків.

# def merging_lists(list_1, list_2):
#     merged_list = list_1 + list_2
#     return merged_list
#
#
# list_1 = my_list
# list_2 = [5, 8, 6, 1, 3, 7, 9, 5, 3, 1]
#
# result = merging_lists(list_1, list_2)
# print(result)


# Завдання 6
#
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.

def exponent_number(numbers, exponent):
    new_list = []
    for number in numbers:
        new_list.append(number ** exponent)
    return new_list


exponent = 2
result = exponent_number(my_list, exponent)
print(result)
