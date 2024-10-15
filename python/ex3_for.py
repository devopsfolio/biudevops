# Создай список от 1 до 20.
myautolist = list(range(1,21))

# Используя цикл и условие, создай два новых списка: один с четными числами, а второй с нечетными.
myevenlist = []
myoddlist = []
for item in myautolist:
    if item % 2 == 0:
        myevenlist.append(item)
    else:
        myoddlist.append(item)
# Выведи оба списка.
print(myevenlist)
print(myoddlist)

