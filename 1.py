a = 9.21
email_count = 2
name_user = 'John'
enable = True

print('a=', a, 'Имя:', name_user, 'Количество писем:', email_count, 'Режим без звука', enable)
a = input('Введите новое а: ')
name_user = input('Введите новое имя: ')
email_count = input('Введите новое количество писем: ')
enable = bool(int(input('Введите 1 если режим без звука или введите 0 ')))
print('a=', a, 'Имя:', name_user, 'Количество писем:', email_count, 'Режим без звука', enable)