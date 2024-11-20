from cryptography.fernet import Fernet
import paramiko

# Расшифровка пароля
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

with open("password.enc", "rb") as password_file:
    encrypted_password = password_file.read()

password = cipher_suite.decrypt(encrypted_password).decode()

# Подключение через Paramiko
hostname = "192.168.1.100"
username = "user"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname, username=username, password=password)

sftp = ssh_client.open_sftp()
sftp.put("local_file.txt", "/remote/path/remote_file.txt")

sftp.close()
ssh_client.close()
print("Файл успешно загружен!")
