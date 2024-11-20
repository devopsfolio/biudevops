import paramiko

class RemoteFileManager:
    def __init__(self, hostname, username, password, port=22):
        """
        Инициализирует подключение к удалённому серверу.
        :param hostname: IP или доменное имя удалённого хоста
        :param username: Имя пользователя для SSH
        :param password: Пароль для SSH
        :param port: Порт для SSH (по умолчанию 22)
        """
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.sftp = None
        self.ssh_client = None

    def connect(self):
        """Устанавливает SSH и SFTP соединение."""
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(
                hostname=self.hostname,
                username=self.username,
                password=self.password,
                port=self.port
            )
            self.sftp = self.ssh_client.open_sftp()
            print("Соединение установлено!")
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            self.disconnect()

    def disconnect(self):
        """Закрывает SFTP и SSH соединение."""
        if self.sftp:
            self.sftp.close()
        if self.ssh_client:
            self.ssh_client.close()
        print("Соединение закрыто.")

    def upload_file(self, local_path, remote_path):
        """
        Копирует файл с локального компьютера на удалённый.
        :param local_path: Путь к локальному файлу
        :param remote_path: Путь к файлу на удалённом сервере
        """
        try:
            self.sftp.put(local_path, remote_path)
            print(f"Файл {local_path} успешно загружен в {remote_path}.")
        except Exception as e:
            print(f"Ошибка загрузки файла: {e}")

    def download_file(self, remote_path, local_path):
        """
        Копирует файл с удалённого компьютера на локальный.
        :param remote_path: Путь к файлу на удалённом сервере
        :param local_path: Путь к файлу на локальном компьютере
        """
        try:
            self.sftp.get(remote_path, local_path)
            print(f"Файл {remote_path} успешно скачан в {local_path}.")
        except Exception as e:
            print(f"Ошибка скачивания файла: {e}")

# Пример использования:
if __name__ == "__main__":
    remote_manager = RemoteFileManager(
        hostname="192.168.1.100", 
        username="user", 
        password="password"
    )
    
    remote_manager.connect()
    remote_manager.upload_file("local_file.txt", "/remote/path/remote_file.txt")
    remote_manager.download_file("/remote/path/remote_file.txt", "downloaded_file.txt")
    remote_manager.disconnect()
