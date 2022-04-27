user_s = input('Введите несколько слов через пробел: ')

for i in enumerate(user_s.split(), start=1):
    print((i[0]), i[1][:10])
