import paramiko
import getpass

#password = getpass.getpass("Введите пароль: ")
#print("Пароль успешно получен (но не отображается).")

hostname = "192.168.1.100"
username = "user"
password = getpass.getpass("Введите пароль: ")

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname, username=username, password=password)

sftp = ssh_client.open_sftp()
sftp.put("local_file.txt", "/remote/path/remote_file.txt")

sftp.close()
ssh_client.close()
print("Файл успешно загружен!")