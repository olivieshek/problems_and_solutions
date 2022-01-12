alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet += alphabet.upper()

user_choice = 0
while user_choice == 0:
	print('    1 - зашифровать и расшифровать текст')
	print('    2 - расишифровать текст')
	user_choice = input('Выберите вариант: ')
	if user_choice == 1:
		text = input('Введите текст для шифрования: ')
		shift = int(input('Введите шаг для шифрования: '))
	elif user_choice == 2:
		encrypted_text = input('Введите текст: ')
	else:
		exit

# text = 'стасичка кавров'
# shift = 4
def encrypt(text: str, shift: int) -> str:
	result = str()
	index = []
	for letter in text:
		if letter in alphabet:
			index = alphabet.index(letter)
			index = (index + shift) % len(alphabet)
			result += alphabet[index]
		else:
			result += letter
	return result

def decrypt(text: str, shift: int, func=encrypt(text, shift)) -> str:
	result = encrypt(text, shift * -1)
	return result

encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

# # принтим
# print(f'"{encrypted_text}" - зашифровали')
# print(f'"{decrypted_text}" - расшифровали')

for i in range(len(alphabet)):
	decrypted_text = decrypt(encrypted_text, i)
	print(f'{i}: {decrypted_text}')
