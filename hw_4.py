# Домашнее задание 4
# # Домашнее задание на тему "Списки в Python":


# # Задание 1:
# # 1. Создайте список `numbers` с пятью произвольными числами.
numbers = [1,0,3,4,5]
print(numbers)
# # 2. Выведите третий элемент списка `numbers`.
print(numbers[2])
# # 3. Добавьте число 10 в конец списка `numbers`.
# numbers.append("10")
numbers.append(10)
print(numbers)
# # 4. Удалите второй элемент из списка `numbers` и выведите список.
numbers.pop(1)
print(numbers)



# # Задание 2:
# # 1. Создайте список `fruits` с тремя названиями фруктов.
fruits = ["apple","pich", "mango"]
# # 2. Объедините списки `numbers` и `fruits` в один новый список `combined`.
print(numbers + fruits)
combined = numbers + fruits
print(combined)
# # 3. Проверьте, сколько элементов находится в списке `combined`.
print(len(combined))
# # 4. Выведите последний элемент списка `combined`.
print(combined[-1])
# # 5. Создайте срез списка `combined`, который включает в себя элементы со второго по четвертый (включительно).
print((combined[1:5]))
# #


# # Задание 3:
# # 1. Создайте копию списка `combined` с помощью среза и присвойте его переменной `combined_copy`.
combined_copy = combined[:]
print(combined_copy)
print(id(combined_copy))
print(id(combined))

# # 2. Поменяйте значение первого элемента списка `combined_copy` на "яблоко".
combined_copy[0] = "яблоко"
print(combined_copy)
# # 3. Выведите исходный список `combined` и список `combined_copy` после изменения.
print(combined_copy)
print(combined)
print(id(combined_copy))
print(id(combined))
