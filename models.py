class DB:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

class Person:
    def __init__(self, name, emai):
        self.name = name
        self.email = email

    def walk(self):
        print("running")

class User(Person):
    def __init__(self, name, email, password):
        Person.__init__(self, name, emai)
        self.password = password

    def walk(self):
        Person.walk(self, )
        print("walking")


class Andelan(Person):

    def __init__(self, name, email, cohort, password=None,):
        Person.__init__(self, name, email, password)
        self.cohort = cohort
