def simple_decorator(func):
    def wrapper():
        print("Декорируем!")
        func()
    return wrapper

@simple_decorator
def greet():
    print("Hi!")

greet()
