import os
import pyaes
## ABRIR O ARQUIVO PRA SER CRIPTOGRAFADO

file_name = 'texto.txt'
file = open(file_name, "rb")
file_data = file.read()
file.close()

## REMOVER O ARQUIVO ORIGINAL
os.remove(file_name)

#CHAVE DE CRIPTOGRAFIA
key = b"1234567890123456"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

#salvar o arquivo criptografado
new_file_name = file_name + '.enc'
new_file = open(f'{new_file_name}', "wb")
new_file.write(crypto_data)
new_file.close()
print("Arquivo criptografado com sucesso!")
