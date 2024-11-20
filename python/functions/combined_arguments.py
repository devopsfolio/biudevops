# Можно комбинировать позиционные и именованные аргументы, 
# но позиционные должны передаваться до именованных.

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("dog", pet_name="Rex")

# Если попробовать передать именованный аргумент 
# перед позиционным, произойдет ошибка:
# describe_pet(pet_name="Rex", "dog")  # Ошибка синтаксиса!


