result = []
user_num = True
total_num = []

while user_num:
    user_num = input('Введите сисла через пробел: ').split()
    total_num.extend(user_num)
    result = [int(item) for item in total_num]
    print(sum(result))
