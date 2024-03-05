from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class AES128:
    def __init__(self, key):
        self.__key = key.encode()[:16]

    def encrypt(self, plaintext):
        cipher = AES.new(self.__key, AES.MODE_ECB)
        encrypted_message = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        return base64.b64encode(encrypted_message).decode()

    def decrypt(self, ciphertext):
        cipher = AES.new(self.__key, AES.MODE_ECB)
        decrypted_message = unpad(cipher.decrypt(base64.b64decode(ciphertext.encode())), AES.block_size)
        return decrypted_message.decode()

    def encryptFile(self, file_bytes):
        cipher = AES.new(self.__key, AES.MODE_ECB)
        encrypted_file = cipher.encrypt(pad(file_bytes, AES.block_size))
        return base64.b64encode(encrypted_file)

    def decryptFile(self, encrypted_file_bytes):
        cipher = AES.new(self.__key, AES.MODE_ECB)
        decrypted_file = unpad(cipher.decrypt(base64.b64decode(encrypted_file_bytes)), AES.block_size)
        return decrypted_file



def main():
    key = input("Введите 16-символьный ключ: ")
    unit = AES128(key)

    text = input("Введите текст для шифрования: ")
    encrypted_text = unit.encrypt(text)
    print("Зашифрованный текст:", encrypted_text)

    decrypted_text = unit.decrypt(encrypted_text)
    print("Расшифрованный текст:", decrypted_text)

    filename = input("Директорию файла и само название файла с его расширением, чтобы его зашифровать: ")
    with open(filename, "rb") as file:
        file_bytes = file.read()
    encrypted_file = unit.encryptFile(file_bytes)
    print("Зашифрованный файл:", encrypted_file)

    decrypted_file = unit.decryptFile(encrypted_file)
    with open("decrypted_file.txt", "wb") as file:
        file.write(decrypted_file)
    print("Расшифрованный файл сохранен в decrypted_file.txt.")



if (__name__ == "__main__"):
    main()