# Создай список из 10 случайных чисел
import random
# два способа создания рандомных списков
myrandomlist1 = list(random.randint(1, 100) for _ in range(10))
myrandomlist2 = [random.randint(100, 1000) for _ in range(10)]

# Найди максимальное и минимальное значения списка используя цикл.
mini = myrandomlist1[0]
maxi = 0
for item in myrandomlist1:
    if item < mini:
        mini = item
    if item > maxi:
        maxi = item
print(myrandomlist1)
print("Минимальное значение списка 1 : "+ str(mini))
print("Максимальное значение списка1 : "+ str(maxi))

# Найди максимальное и минимальное значения с помощью функции
print(myrandomlist2)
print("Минимальное значение списка 2 : " + str(min(myrandomlist2)))
print("Максимальное значение списка 2 : " + str(max(myrandomlist2)))
