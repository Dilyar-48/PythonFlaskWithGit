from flask import Flask, url_for, request, redirect, session, render_template
import json
from forms.loginform import LoginForm
from forms.user import RegisterForm
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../static/img/'
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
LIST_OF_PICTURES_TO_GALERY = ["../static/img/slide1.png", "../static/img/slide2.png",
                              "../static/img/slide3.png", "../static/img/slide4.png",
                              "../static/img/slide5.png"]


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась" width="300">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась" width="300">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-primary" role="alert" style='color: green; background-color: #98FB98;'>
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-primary" role="alert" style='color: blue; background-color: #7FFFD4;'>
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-primary" role="alert" style='color: #BDB76B; background-color: #F0E68C;'>
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-primary" role="alert" style='color: #C71585; background-color: #FFB6C1;'>
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center" style='color: black;'>Анкета претендента</h1>
                            <h3 align="center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                    <label for="name"></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное общее</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <label>Какие у вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Строитель</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер по терраформированию</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Климатолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Специалист по радиационной защите</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Астрогеолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Гляциолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Другое</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                     <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов отстаться на марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "<h1 align='center'>Форма отправлена</h1>"


@app.route('/choice/<string:planet_name>')
def choice(planet_name):
    to_planet_choice = {
        "Марс": ["близка к Земле", "Марс известен как Красная планета",
                 "На Марсе существуют огромные каньоны и вулканы",
                 "Ученые обнаружили на Марсе следы воды в прошлом", "На Марсе есть ледяные шапки"],
        "Юпитер": ["не сильно близка к Земле", "Юпитер — самая крупная планета Солнечной системы",
                   "На Юпитере нет твёрдой поверхности",
                   "Вокруг Юпитера вращаются 79 известных нам спутников",
                   "Магнитное поле Юпитера — самое мощное в Солнечной системе"],
        "Меркурий": ["самая близкая к Земле", "Его поверхность покрыта кратерами и напоминает Луну.",
                     "На Меркурии практически нет атмосферы.",
                     "День на Меркурии длится дольше, чем год.",
                     "Температура на Меркурии может колебаться от очень высокой до экстремально низкой."],
        "Венера": ["самая близкая к Земле", "Является второй планетой от Солнца и часто называется 'сестрой Земли'",
                   "Поверхность Венеры покрыта густыми облаками из серной кислоты.",
                   "Температура на поверхности достигает +470°C.",
                   "День на Венере длится дольше, чем год."],
        "Земля": ["единственная известная нам планета, на которой существует жизнь.",
                  "Она вращается вокруг Солнца и имеет один естественный спутник - Луну.",
                  "Поверхность Земли состоит из разнообразных ландшафтов.",
                  "Наша планета обладает уникальной атмосферой.",
                  "Земля является домом для миллионов видов живых существ."],
        "Сатурн": ["шестая от Солнца и одна из самых ярких на ночном небе.",
                   "Известна своими впечатляющими кольцами, которые состоят из льда и камня.",
                   "Имеет множество спутников, среди которых выделяются Титан и Энцелад.",
                   "На Сатурне дуют сильнейшие ветры, достигающие скорости до 1800 км/ч.",
                   "Сатурн назван в честь римского бога сельского хозяйства."],
        "Уран": ["седьмая по удалённости от Солнца.",
                 "Имеет голубое свечение из-за метана в его атмосфере.",
                 "Эта планета уникальна тем, что вращается «на боку».",
                 "Уран был открыт в 1781 году английским астрономом Уильямом Гершелем.",
                 "На Уране наблюдаются сильные ветры, дующие в направлении вращения планеты."],
        "Нептун": ["восьмая от Солнца в нашей Солнечной системе.",
                   "Он был открыт в 1846 году благодаря математическим расчётам.",
                   "Имеет глубокий синий цвет, который ему придаёт метан в атмосфере.",
                   "На Нептуне дуют самые сильные ветры в Солнечной системе, достигающие скорости до 2100 км/ч.",
                   "Планета названа в честь римского бога морей ."]
    }
    if planet_name.capitalize() in to_planet_choice:
        my_choice = to_planet_choice[planet_name.capitalize()]
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                      </head>
                      <body>
                        <h1 style='color: black;'>Моё предложение - {planet_name.capitalize()}</h1>
                        <h4>Эта планета {my_choice[0]}</h4>
                        <div class="alert alert-primary" role="alert" style='color: green; background-color: #98FB98;'>
                          {my_choice[1]}
                        </div>
                        <div class="alert alert-primary" role="alert" style='color: blue; background-color: #7FFFD4;'>
                          {my_choice[2]}
                        </div>
                        <div class="alert alert-primary" role="alert" style='color: #BDB76B; background-color: #F0E68C;'>
                          {my_choice[3]}
                        </div>
                        <div class="alert alert-primary" role="alert" style='color: #C71585; background-color: #FFB6C1;'>
                          {my_choice[4]}
                        </div>
                      </body>
                    </html>'''
    else:
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                              </head>
                              <body>
                                <h1 style='color: black;'>Эта планета мне неизвестна!</h1>
                                <h4>Попробуйте писать запрос корректно, русскими буквами!</h4>
                              </body>
                            </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                      </head>
                      <body>
                        <h1 style='color: black;'>Результаты отбора</h1>
                        <h3>Претендента на участие в миссии {nickname}:</h3>
                        <div class="alert alert-primary" role="alert" style='color: green; background-color: #98FB98;'>
                          Поздравляем! Ваш рейтинг после {level} этапа отбора...
                        </div>
                        <h3>Составляет {rating}!</h3>
                        <div class="alert alert-primary" role="alert" style='color: #BDB76B; background-color: #F0E68C;'>
                          Желаем удачи!
                        </div>
                      </body>
                    </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                               <html lang="en">
                                 <head>
                                   <meta charset="utf-8">
                                   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                   <link rel="stylesheet"
                                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                   crossorigin="anonymous">
                                   <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                   <title>Пример формы</title>
                                 </head>
                                 <body>
                                   <h1 style='color: black;' align='center'>Загрузка фотографии</h1>
                                   <h3 align='center'>Для участия в миссии</h3>
                                   <div>
                                       <form method="post" enctype="multipart/form-data" class="login_form">
                                       <div class="form-group">
                                            <label for="photo">Выберите файл</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                       </div>
                                       <div class="form-group" style='padding: 7px 0px;'>
                                            <img src="{url_for('static', filename='img/image.png')}" alt="здесь должна была быть картинка, но не нашлась", width='100%'>
                                       </div>
                                       <button type="submit" class="btn btn-primary">Записаться</button>
                                       </form>
                                   </div>
                                 </body>
                               </html>'''

    elif request.method == 'POST':
        image = request.files['file']
        if image:
            image.save(app.config['UPLOAD_FOLDER'].lstrip("../") + "/image.png")
        return redirect("/load_photo")


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
                            integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                            crossorigin="anonymous">
                        <body>
                            <div id="myCarousel" class="carousel slide w-50 ms-auto me-auto" data-bs-ride="carousel">
                              <center><h1>Пейзажи Марса</h1></center>
                              <div class="carousel-inner" role="listbox">
                                <div class="carousel-item active">
                                  <img class="d-block w-100" src="static/img/slide1.png" alt="Первый слайд">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="static/img/slide2.png" alt="Второй слайд">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="static/img/slide3.png" alt="Третий слайд">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="static/img/slide4.png" alt="Четвёртый слайд">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="static/img/slide5.png" alt="Пятый слайд">
                                </div>
                              </div>
                              <a class="carousel-control-prev" href="#myCarousel" role="button" data-bs-target="#myCarousel" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Предыдущий</span>
                              </a>
                              <a class="carousel-control-next" href="#myCarousel" role="button" data-bs-target="#myCarousel" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Следующий</span>
                              </a>
                              <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
                              integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
                              crossorigin="anonymous"></script>
                            </div>
                        </body>
                    </html>'''


@app.route('/training/<string:prof>')
def training(prof):
    return render_template('training.html', prof=prof.capitalize())


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_temp.html', list=list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    my_answer = {
        "title": "Анкета",
        "surname": "Замалиев",
        "name": "Диляр",
        "education": "Основное общее",
        "profession": "Школьник",
        "sex": "Мужской",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True",
    }
    return render_template('auto_answer.html', surname=my_answer["surname"], name=my_answer["name"],
                           education=my_answer["education"], profession=my_answer["profession"], sex=my_answer["sex"],
                           motivation=my_answer["motivation"], ready=my_answer["ready"])


@app.route('/distribution')
def distribution():
    return render_template('cabins.html', user_list=["Ридли Скотт", "Энди Уир"])


@app.route('/table/<sex>/<age>')
def table(sex, age):
    return render_template('marsianins_table.html', sex=sex.lower(), age=int(age))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/true_answer_page')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/true_answer_page')
def true_answer_page():
    return render_template('form_answer.html', title='Авторизация прошла успешно')


@app.route('/member')
def member():
    with open("templates/peoples.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
        for i in news_list['peoples']:
            i['prof'] = ", ".join(sorted(i['prof']))
    return render_template('member_page.html', peoples=news_list)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'GET':
        return render_template('galery_page.html', pictures=LIST_OF_PICTURES_TO_GALERY)
    elif request.method == 'POST':
        image = request.files['file']
        name = image.filename
        if image:
            image.save(app.config['UPLOAD_FOLDER'].lstrip("../") + name)
            LIST_OF_PICTURES_TO_GALERY.append(app.config['UPLOAD_FOLDER'] + name)
        return redirect("/galery")

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
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/true_answer_page')
    return render_template('register.html', title='Регистрация', form=form)

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
    jb = Jobs()
    jb.team_leader = 1
    jb.job = "deployment of residential modules 1 and 2"
    jb.work_size = 15
    jb.collaborators = "2, 3"
    jb.is_finished = False
    session.add(jb)
    session.commit()
    app.run(port=8080, host='127.0.0.1')

if __name__ == '__main__':
    main()