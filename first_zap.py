from flask import Flask, url_for, request, redirect, session, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm
from my_db_add_info import add_new_info

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


if __name__ == '__main__':
    add_new_info()
    app.run(port=5000, host='127.0.0.1')
