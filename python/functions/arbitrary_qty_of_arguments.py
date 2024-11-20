# Звездочка * перед именем позволяет 
# функции принимать любое количество 
# позиционных аргументов в виде кортежа.
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5)

# Две звезды ** позволяет функции принимать любое 
# количество именованных аргументов в виде словаря.
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")

# Совмещение * и ** 
def show_info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_info(1, 2, 3, name="Alice", age=30)

# Если у вас уже есть кортеж или словарь, 
# их можно передать в функцию с помощью * и **.
def greet(greeting, name):
    print(f"{greeting}, {name}!")

args = ("Hello", "Alice")
kwargs = {"greeting": "Hi", "name": "Bob"}

greet(*args)  # Распаковка кортежа
greet(**kwargs)  # Распаковка словаря
