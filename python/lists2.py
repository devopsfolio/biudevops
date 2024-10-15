
import random
# Создай список чисел от 1 до 100
numlist1 = list(range(1, 101))

# Используя цикл и условие, создай новый список, который будет содержать только числа, кратные 5.
mult5 = []
for item in numlist1:
    if item % 5 == 0:
        mult5.append(item)
print("Это все числа кратные пяти:")
print(mult5)

