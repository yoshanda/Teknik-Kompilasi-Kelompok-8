import basic

while True:
		text = input('Kelompok 8 > ')
		result, error = basic.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)