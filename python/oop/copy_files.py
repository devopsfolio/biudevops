import shutil
import os

class FileManager:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def copy_file(self):
        if os.path.exists(self.source):
            shutil.copy2(self.source, self.destination)
            print(f"Файл {self.source} скопирован в {self.destination}")
        else:
            print(f"Файл {self.source} не найден!")

    def move_file(self):
        if os.path.exists(self.source):
            shutil.move(self.source, self.destination)
            print(f"Файл {self.source} перемещён в {self.destination}")
        else:
            print(f"Файл {self.source} не найден!")

# Пример использования:
file_manager = FileManager("example.txt", "/tmp/example.txt")
file_manager.copy_file()
