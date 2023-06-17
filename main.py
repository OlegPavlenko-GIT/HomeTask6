#Задание 1
#Напишите функцию, вычисляющую произведение элементов списка целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result
my_list = [2, 3, 4, 5]
product = multiply_elements(my_list)
print("Product of list elements:", product)
#
#Задание 2
#Напишите функцию для нахождения минимума в списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
def find_minimum(numbers):
    if len(numbers) == 0:
        return None
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value
my_list = [5, 2, 8, 1, 9]
minimum = find_minimum(my_list)
print("Minimum value:", minimum)
#
# Задание 3.
# Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
def count_prime_numbers(numbers):
    count = 0

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in numbers:
        if is_prime(num):
            count += 1

    return count
my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
result = count_prime_numbers(my_list)
print(result)
# Result: 4

# Задание 4
# Напишите функцию, удаляющую из списка целых некоторое заданное число.
# Из функции нужно вернуть количество удаленных элементов.
def remove_element(nums, target):
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] == target:
            nums.pop(i)
            count += 1
        else:
            i += 1
    return count
numbers = [1, 2, 3, 4, 5, 3, 6, 3]
target = 3
removed_count = remove_element(numbers, target)
print("Amount of removed elements:", removed_count)
#
# Задание 5
# Напишите функцию, которая получает два списка в качестве параметра и возвращает список,
# содержащий элементы обоих списков.
def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list
# Example of list
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Function and result
merged = merge_lists(list1, list2)
print(merged)
#
#Задание 6
#Напишите функцию, высчитывающую степень каждого элемента списка целых.
#Значение для степени передаётся в качестве параметра, список тоже передаётся в качестве параметра.
#Функция возвращает новый список, содержащий полученные результаты.
def calculate_powers(nums, power):
    result = []
    for num in nums:
        result.append(num ** power)
    return result
numbers = [2, 3, 4, 5]
power = 2
result = calculate_powers(numbers, power)
print(result)
# Result [4, 9, 16, 25]



