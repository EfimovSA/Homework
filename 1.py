from sys import argv

hours = argv[1]
salary = argv[2]
award = argv[3]
total = (int(hours) * int(salary)) + int(award)
print(f'Заработная плата сотрудника составялет: {total}')
