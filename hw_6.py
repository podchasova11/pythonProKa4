# Домашнее задание  6
# Домашнее задание на тему "Словари в автоматизации":
#
# Задание 1:
# 1. Ознакомьтесь с понятием словарей в Python и узнайте, для чего они используются в автоматизации.
# 2. Создайте словарь `student`, который будет содержать информацию о студенте:
#   - Имя студента (ключ: "name")
#   - Возраст студента (ключ: "age")
#   - Список предметов (type list), которые он изучает (ключ: "subjects")
#   - Средний балл (ключ: "average_score")
from urllib import response

student = {
    "name": "Mila",
    "age": 20,
    "subjects": ["M", "A", "D"],
    "average_score": 10
    }
type_list = ["M", "A", "D"]
print(type_list[0])
print(type_list)

# 3. Выведите на экран значение каждого ключа из словаря `student` с помощью доступа к элементам по ключу.
keys = student.keys()
values = student.values()
print(keys)
# 4. Обновите значение ключа "average_score" в словаре `student` на новое значение (например, 4.75).
student["average_score"] = 4.75
print(student)
# 5. Добавьте новый предмет в список предметов студента (например, "Физика").
print(student["subjects"])
print(student)
sub = "Fizics"
type_list.append(sub)
print(type_list)
print(keys)
print(values)
for keys, values in student.items():
    print(f"Ключ:{keys}, Значение: {values}")
# 6. Удалите ключ "age" из словаря `student`, так как эта информация больше не нужна.
print(student.pop("age"))
print(student)
for keys, values in student.items():
    print(f"Ключ:{keys}, Значение: {values}")
    print(student.keys())
# 7. Проверьте наличие ключей "age" и "gender" в словаре `student`.
# Выведите соответствующее сообщение, если ключ существует или не существует.
print(student.keys())
print(values)

if "name" in student:
    print("Ключ 'name' существует в словаре")
assert "age" in student.keys(), "Элемент 'age' отсутствует в ответе"

assert "gender" in student.keys(), "Элемент 'gender' отсутствует в ответе"
print("Element is present")

# 8. Получите список всех ключей словаря `student` и выведите его на экран.
print(student.keys())

# 9. Получите список всех значений словаря `student` и выведите его на экран.

print(student.values)