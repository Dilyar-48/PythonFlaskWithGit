from flask import Flask, url_for, request, redirect, session, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        hashed = hash(form.password.data)
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            hashed_password=hashed,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/true_answer_page')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/true_answer_page')
def true_answer_page():
    return render_template('form_answer.html', title='Авторизация прошла успешно')


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return render_template("index.html", news=news)


def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    names = ["Ridley", "James", "Yuriy", "Sergey"]
    surnames = ["Scott", "Cameron", "Gagarin", "Petkin"]
    ages = [21, 42, 27, 67]
    positions = ["captain", "colonist", "colonist", "colonist"]
    specialites = ["research engineer", "pilot", "pilot", "research engineer"]
    emails = ["scott_chief@mars.org", "jamesCameron@mars.org", "GagarinYura@mars.org", "SergPet@mars.org"]
    for us in range(len(names)):
        if not session.query(User).filter(User.email == emails[us]).first():
            user = User()
            user.surname = surnames[us]
            user.name = names[us]
            user.age = ages[us]
            user.position = positions[us]
            user.speciality = specialites[us]
            user.address = f"module{us + 1}"
            user.email = emails[us]
            session.add(user)
    jb = Jobs()
    jb.user = 1
    jb.job = "deployment of residential modules 1 and 2"
    jb.work_size = 15
    jb.collaborators = "2, 3"
    jb.is_finished = False
    if not session.query(Jobs).filter(Jobs.team_leader == jb.team_leader, Jobs.job == jb.job,
                                      Jobs.work_size == jb.work_size, Jobs.collaborators == jb.collaborators).first():
        session.add(jb)
    session.commit()


if __name__ == '__main__':
    main()
    app.run(port=5000, host='127.0.0.1')
