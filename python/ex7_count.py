# Подсчет элементов
# Создай список случайных чисел от 1 до 10, включающих повторяющиеся значения
import random
myrandomlist = list(random.randint(1, 10) for _ in range(10))
# подсчитай количество каждого элемента в списке
# с использование генератора словаря
mygendict = {i: myrandomlist.count(i) for i in myrandomlist}
print(mygendict)
# с использованием каунтера
from collections import Counter
mycountedict = Counter(myrandomlist)
print(mycountedict)