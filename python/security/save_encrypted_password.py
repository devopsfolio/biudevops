from cryptography.fernet import Fernet

# Генерация ключа шифрования (делается один раз, ключ хранится безопасно)
# key = Fernet.generate_key()
# with open("key.key", "wb") as key_file:
#     key_file.write(key)

# Загрузка ключа из файла
with open("key.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Шифрование пароля (делается один раз)
# encrypted_password = cipher_suite.encrypt(b"my_secure_password")
# with open("password.enc", "wb") as password_file:
#     password_file.write(encrypted_password)

# Расшифровка пароля
with open("password.enc", "rb") as password_file:
    encrypted_password = password_file.read()

password = cipher_suite.decrypt(encrypted_password).decode()

print(f"Расшифрованный пароль: {password}")
