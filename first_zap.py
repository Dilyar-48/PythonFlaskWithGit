from flask import Flask, jsonify, request, redirect, abort, render_template, make_response
from data import db_session, jobs_api, user_api
from data.departament import Department
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm
from my_db_add_info import add_new_info
from flask_login import LoginManager, login_user, login_required, logout_user
from forms.autorize_form import LoginForm
from forms.add_task_form import AddJobForm
from flask_login import current_user
from forms.add_deps_form import AddDepForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


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
            city_from=form.city_from.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


@app.route("/deps")
def deps():
    db_sess = db_session.create_session()
    deps = db_sess.query(Department).all()
    return render_template("deps.html", deps=deps)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('autorize.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('autorize.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/jobs', methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = AddJobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.job = form.title.data
        jobs.work_size = form.work_size.data
        jobs.is_finished = form.is_finished.data
        jobs.collaborators = form.collaborators.data
        jobs.team_leader = form.team_leader.data
        jobs.category_id = form.category_id.data
        user = db_sess.query(User).filter(User.id == jobs.team_leader).first()
        user.jobs.append(jobs)
        db_sess.merge(user)
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Добавление работы',
                           form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = AddJobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if jobs:
            form.title.data = jobs.job
            form.work_size.data = jobs.work_size
            form.is_finished.data = jobs.is_finished
            form.collaborators.data = jobs.collaborators
            form.team_leader.data = jobs.team_leader
            form.category_id.data = jobs.category_id
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if jobs:
            jobs.job = form.title.data
            jobs.work_size = form.work_size.data
            jobs.is_finished = form.is_finished.data
            jobs.collaborators = form.collaborators.data
            jobs.team_leader = form.team_leader.data
            jobs.category_id = form.category_id.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html',
                           title='Редактирование работы',
                           form=form
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/departaments', methods=['GET', 'POST'])
@login_required
def add_deps():
    form = AddDepForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        deps = Department()
        deps.title = form.title.data
        deps.members = form.members.data
        deps.email = form.email.data
        deps.chief = form.chief.data
        user = db_sess.query(User).filter(User.id == deps.chief).first()
        user.deps.append(deps)
        db_sess.merge(user)
        db_sess.commit()
        return redirect('/deps')
    return render_template('add_dep.html', title='Добавление департамента',
                           form=form)


@app.route('/departaments/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_deps(id):
    form = AddDepForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        deps = db_sess.query(Department).filter(Department.id == id).first()
        if deps:
            form.title.data = deps.title
            form.members.data = deps.members
            form.email.data = deps.email
            form.chief.data = deps.chief
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        deps = db_sess.query(Department).filter(Department.id == id).first()
        if deps:
            deps.title = form.title.data
            deps.members = form.members.data
            deps.email = form.email.data
            deps.chief = form.chief.data
            db_sess.commit()
            return redirect('/deps')
        else:
            abort(404)
    return render_template('add_dep.html',
                           title='Редактирование департамента',
                           form=form
                           )


@app.route('/departaments_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def departament_delete(id):
    db_sess = db_session.create_session()
    deps = db_sess.query(Department).filter(Department.id == id).first()
    if deps:
        db_sess.delete(deps)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/deps')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

if __name__ == '__main__':
    add_new_info()
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(user_api.blueprint)
    app.run(port=5000, host='127.0.0.1')
