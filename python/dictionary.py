import random
from collections import Counter
# Создай список случайных чисел от 1 до 10, включающих повторяющиеся значения
numlist2 = [random.randint(1, 10) for _ in range(20)]
print("это список с повторяющимися значениями")
print(numlist2)
numdict = {i:numlist2.count(i) for i in numlist2}
print("сколько повторяется каждое значение")
print(numdict)
print("или в столбик")
for key, value in numdict.items():
    print(f"{key}: {value}")

print("или с использованием Counter:")
numdict2 = Counter(numlist2)
print(numdict2)

