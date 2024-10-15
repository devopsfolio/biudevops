import random


mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("вывожу элементы списка")
for element in mylist1:
    print(element)

print("Сумма всех элементов списка")
sum = 0
for element in mylist1:
    sum = sum + element

print(sum)

print("Произведение всех элементов списка")
prod = 1
for element in mylist1:
    prod = prod * element

print(prod)

print("Первые три элемента списка")
print(mylist1[:3])
print("Последние пять элементов списка")
print(mylist1[-5:])
print("Список в обратном порядке")
print(mylist1[::-1])

mylist2 = list(range(1,21))
myevenlist = []
myoddlist = []
for element in mylist2:
    if element % 2 == 0:
        myevenlist.append(element)
    else:
        myoddlist.append(element)
print("это четный список")
print(myevenlist)
print("это нечетный список")
print(myoddlist)

# create list witn random numbers
mylist3 = [random.randint(1, 100) for _ in range(10)]
print("это рандомный список")
print(mylist3)
myduplist = []
for item in mylist3:
    myduplist.append(item * 2)
print("каждый элемент списка умноженый на 2")
print(myduplist)

mylist4 = [random.randint(100, 1000) for _ in range(10)]
max = mylist4[0]
for item in mylist4:
    if item > max:
        max = item
print("это максимальное число из списка mylist4")
print(max)
