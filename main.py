from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    names = ["Ridley", "James", "Yuriy"]
    surnames = ["Scott", "Cameron", "Gagarin"]
    ages = [21, 42, 27]
    positions = ["captain", "colonist", "colonist"]
    specialites = ["research engineer", "pilot", "pilot"]
    emails = ["scott_chief@mars.org", "jamesCameron@mars.org", "GagarinYura@mars.org"]
    for us in range(len(names)):
        user = User()
        user.surname = surnames[us]
        user.name = names[us]
        user.age = ages[us]
        user.position = positions[us]
        user.speciality = specialites[us]
        user.address = f"module{us + 1}"
        user.email = emails[us]
        session.add(user)
    session.commit()
    app.run()

if __name__ == '__main__':
    main()