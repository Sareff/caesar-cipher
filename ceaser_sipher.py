def encrypt(s, n):
	global alphabet
	res = ''
	for c in s:
		res += alphabet[alphabet.index(c) + (n) % len(alphabet)]
	return res

def decrypt(s):
	global alphabet
	ca = 0
	fa = {}
	for c in range(len(alphabet)):
		for i in range(len(s)):
			if s[i]==alphabet[c]:
				ca += 1
		ca = ca * 100 / len(s)
		fa[alphabet[c]] = ca
		ca = 0

	for k in range()


choice = int(input('Шифруем(1) или Расшифровываем(2)? '))
if choice == 1:
	lang = 0
	while lang != 1 or lang != 2:
		lang = int(input('Какой алфавит использовать? кириллица(1) или латиница(2): '))
		if lang == 1:
			alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
			break
		elif lang == 2:
			alphabet = 'abcdefghijklmnopqrstuvwyxz'
			break
		else:
			print('Вы ввели не то число, попробуйте снова...')

	s = input('Введите строку, котороую хотите зашифровать: ')
	n = int(input('Введите ROT: '))
	print('Шифротекст:', encrypt(s, n))

elif choice == 2:
	s = input('Введите строку которую хотите рашифровать: ')

