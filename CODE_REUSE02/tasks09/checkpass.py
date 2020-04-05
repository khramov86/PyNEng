def check_passwd(username, password, min_length=8, check_username=True):
    if len(password) < min_length and check_username:
        print('Пароль слишком короткий')
        return False
    elif check_username and username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True


username_passwd = [{'username': 'cisco', 'password': 'cisco', 'check_username': False},
                   {'username': 'nata', 'password': 'natapass'},
                   {'username': 'user', 'password': '123456789'}
                   ]

if __name__ == '__main__':
    for data in username_passwd:
        print(data)
        # Python распаковывает словарь и передает его в функцию как ключевые аргументы превращается в вызов вида
        # check_passwd(username='cisco', password='cisco'
        check_passwd(**data)
