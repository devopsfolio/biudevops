# Фильтрация массива
# Создай список чисел от 1 до 100.
myseqlist = list(range(1, 101))

# Используя цикл и условие, создай новый список, который будет содержать только числа, кратные 5.
mymultfive = []
for item in myseqlist:
    if item % 5 == 0:
        mymultfive.append(item)

print(mymultfive)