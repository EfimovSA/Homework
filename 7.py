def int_func(user_text=''):
    return user_text[0].upper() + user_text[1:]


print(int_func('text'))

for item in 'text text text'.split():
    print(int_func(item), end=' ')
