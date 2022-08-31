class User:
    count_users = 0

    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password
        if isinstance(self, User):
            User.count_users += 1

    @property
    def login(self):
        return self.__login

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def _set_password(self, value):
        self.__password = value

    password = property(fset=_set_password)

    def show_info(self):
        print(f'name: {self.__name} \nlogin: {self.__login}')


class SuperUser(User):
    count_super_users = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.__role = role
        SuperUser.count_super_users += 1
        User.count_users -= 1 #чтобы SuperUser не учитывался в счетчике класса User(надо по заданию)

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    def show_info(self):
        print(f'name: {self.name} \nlogin: {self.login} \nrole: {self.role}')


user1 = User('Paul McCartney', 'paul', '1234')
user2 = User('George Harrison', 'george', '5678')
user3 = User('Richard Starkey', 'ringo', '8523')
admin = SuperUser('John Lennon', 'john', '0000', 'admin')

user1.show_info()
admin.show_info()

users = User.count_users
admins = SuperUser.count_super_users

print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')

print(user3.name)
user3.name = 'Ringo Starr'
print(user3.name)

print(user2.login)
user2.login = 'geo' #ошибка

user1.password = 'Pa$$w0rd'
print(user2.password) #ошибка
