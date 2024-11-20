class MyClass:
    def __init__(self, param1, param2):
        """
        Конструктор класса MyClass.
        :param param1: первый параметр
        :param param2: второй параметр
        """
        self.param1 = param1
        self.param2 = param2

    def show_params(self):
        """
        Метод для вывода параметров.
        """
        print(f"param1: {self.param1}, param2: {self.param2}")
