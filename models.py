class DB:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Andelan(User):

    def __init__(self, name, email, password, cohort):
        User.__init__(self, name, email, password, cohort)
        
        self.cohort = cohort
