user_goods = True
total_goods = []
total_goods_nonam = []
n = 1
a = []
b = []
c = []
d = []
result = {}
while user_goods:
    user_goods = input('Введи через пробел Наименование товара, Стоимость, Количество и Ед. измерения: ').split()
    new = {'название': user_goods[0], 'цена': user_goods[1],
           'количество': user_goods[2], 'ед': user_goods[3]}
    total_goods_nonam.append(new)
    total_goods.append((n, new))
    n += 1

    for i in total_goods_nonam:
        a.append((i.get('название')))
        b.append(int(i.get('цена')))
        c.append(int(i.get('количество')))
        d.append((i.get('ед')))

    result = {'название': a, 'цена': b, 'количество': c, 'ед': d}

    print('итог', total_goods)
    print('анализ ', result)

    a.clear()
    b.clear()
    c.clear()
    d.clear()
