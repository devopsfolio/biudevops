# Декоратор — это функция, которая принимает другую 
# функцию и расширяет её функциональность.

# Основная концепция
# Декораторы оборачивают функции. Пример:

def decorator(func):
    def wrapper():
        print("Перед вызовом функции.")
        func()
        print("После вызова функции.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
