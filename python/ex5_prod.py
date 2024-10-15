# Умножение элементов массива на 2
# Создай список из 10 случайных чисел.
import random
myrandomlist = list(random.randint(1, 101) for _ in range(10))

# Используя цикл, умножь каждый элемент списка на 2 и сохрани результат в новый список.
myduplist = []
for item in myrandomlist:
    myduplist.append(item * 2)

# Выведи оба списка для сравнения.
print(myrandomlist)
print(myduplist)

