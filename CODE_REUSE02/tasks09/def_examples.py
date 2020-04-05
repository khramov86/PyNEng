from CODE_REUSE02.tasks09 import checkpass


def add_user_to_users_file(user, users_filename='users.txt', **kwargs):
    while True:
        passwd = input(f'Введите пароль для пользователя {user}: ')
        if checkpass.check_passwd(user, passwd, **kwargs):
            break

    with open(users_filename, 'a') as f:
        f.write(f'{user}, {passwd}\n')


add_user_to_users_file(user='vkhramov', check_username=True, min_length=6)
