def info(name_user='Имя', surname_user='Фамилия', dob_user='Дата рождения',
         town_user='Город', email_user='Email', phone_user='Телефон'):
    print('Имя пользователя:', name_user, 'Фамилия:', surname_user, 'Дата рождения:', dob_user,
          'Город:', town_user, 'Email:', email_user, 'Телефон:', phone_user)


name = input('Имя пользователя: ')
surname = input('Фамилия пользователя: ')
dob = input('Дата рождения: ')
town = input('Город: ')
email = input('Email: ')
phone = input('Телефон: ')
info(name, surname, dob, town, email, phone)
