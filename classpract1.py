class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль.
    """

    def __init__(self, username, password, password_confirm):
        if password != password_confirm:
            raise ValueError("Пароли не совпадают")
        if not username or not password:
            raise ValueError("Логин и пароль не могут быть пустыми")
        self.username = username
        self.password = password


class Database:
    """
    Класс, сохраняющий логин и пароль пользователя в словарь (ключ:значение)
    """

    def __init__(self):
        self.data = {}

    def add_user(self, user):
        if user.username in self.data:
            raise ValueError("Пользователь уже существует")
        self.data[user.username] = user.password


if __name__ == '__main__':
    data = Database()

    while True:
        try:
            username = input('Введите логин: ')
            password = input('Введите пароль: ')
            password_confirm = input('Подтвердите пароль: ')
            user = User(username, password, password_confirm)
            data.add_user(user)
            print(f"Пользователь {user.username} успешно добавлен!")
        except ValueError as error_message:
            print(error_message)

        cont = input("Добавить еще одного пользователя? (да/нет): ")
        if cont.lower() != 'да':
            break
