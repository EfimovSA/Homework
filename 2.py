second_value = int(input('Введите время в секундах: '))
print('{}:{}:{}'.format(second_value//3600, (second_value // 60 - second_value//3600*60), second_value % 60))