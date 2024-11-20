class LogProcessor:
    def __init__(self, log_file):
        self.log_file = log_file

    def search_keyword(self, keyword):
        try:
            with open(self.log_file, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if keyword in line:
                        print(f"Найдено: {line.strip()}")
        except FileNotFoundError:
            print(f"Файл {self.log_file} не найден.")

# Пример использования:
log_processor = LogProcessor("/var/log/system.log")
log_processor.search_keyword("error")

