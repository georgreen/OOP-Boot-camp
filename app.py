from models import DB, User, Andelan

app_db = DB()

def add_user(name, email, password, cohort=None, user_type='Normal'):
    if user_type == 'Normal':
        new_user = User(name, email, password)
    else:
        new_user = Andelan(name, email, password, cohort)

    app_db.add_user(new_user)
    print('New user added succesfully.')


add_user('test_user', 'test_user@gmail.com', 'veryhardtogeuss')
# add_user('test_Andelan', 'test_andelan@gmail.com', 'veryhardtogeuss',
#          cohort=10, user_type='Andelan')

app = Flask(__name__)
