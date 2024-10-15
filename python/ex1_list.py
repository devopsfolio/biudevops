# Упражнение 1: Работа с массивами
# Создай список чисел от 1 до 10.
# вручную
mylist_man = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# автоматически
mylist_auto = list(range(11, 21))

# обьединим его в один список
# 1. конкатенация
mylist1 = mylist_man + mylist_auto
# 2. с использованием метода
mylist2 = mylist_man
mylist2.extend(mylist_auto)

# Выведи его элементы с помощью цикла for.
for item in mylist1:
    print(item)
for item in mylist2:
    print(item)

# Найди произведение всех элементов списка.
# с помощью цикла
count = 1
for item in mylist1:
    count *= item
print(count)
# с помощью метода
from math import prod
print(prod(mylist1))

# проверим содержимое списка mylist_man
print(mylist_man)
# содержимое mylist_man изменилось  
# так же кае и содержимое mylist2
# после манипуляций в строках 12, 13

