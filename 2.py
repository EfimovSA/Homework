list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = (i for j, i in enumerate(list) if list[j - 1] < list[j] and j > 0)
print([i for i in new_list ])
