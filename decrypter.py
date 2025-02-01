import os
import pyaes
## ABRIR O ARQUIVO
file_name = 'texto.txt'
file = open(file_name, "rb")
file_data = file.read()
file.close()
## CHAVE DE DESCRIPTOGRAFIA
key = b"1234567890123456"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data =aes.decrypt(file_data)
## REMOVE O ARQUIVO CRIPTOGRAFADO
os.remove(file_name)

## CRIAR UM NOVO ARQUIVO DESCRIPTOGRAFADO
new_file_name = "texto_novo.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
