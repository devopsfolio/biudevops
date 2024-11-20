# Декоратор с аргументами
# Это декоратор, который принимает дополнительные параметры, 
# передаваемые при его создании. 
# Такие параметры помогают настроить поведение декоратора.

#  Общий шаблон
def decorator_with_arguments(arg1, arg2):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            # Используем аргументы декоратора (arg1, arg2)
            print(f"Декоратор использует аргументы: {arg1}, {arg2}")
            # Вызываем саму функцию
            result = func(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator


# Пример: Логирование уровня доступа
# Допустим, у нас есть система, в которой нужно логировать 
# вызовы функций с указанием уровня доступа (admin, user).
def access_level(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level.upper()}]: Вызов функции {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Теперь используем декоратор:
@access_level("admin")
def delete_user(user_id):
    print(f"Пользователь с ID {user_id} удалён.")

@access_level("user")
def view_profile(user_id):
    print(f"Профиль пользователя с ID {user_id}.")

# Вызов функций:
delete_user(42)
view_profile(42)


# Другой пример: Повторное выполнение функции
# Если нужно повторить выполнение функции несколько раз, 
# можно сделать декоратор с параметром, задающим количество повторов.
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Выполнение {i + 1}")
                result = func(*args, **kwargs)   # Вызываем оригинальную функцию
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Привет!")
# Вызов функции:
say_hello()

@repeat(2)
def add(a, b):
    print(f"Суммируем {a} и {b}")
    print(a + b)
# Вызов функции:
add(105, 381)



