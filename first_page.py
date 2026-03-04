from flask import Flask, url_for, request, redirect, session, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/img'
app.secret_key = 'supersecretkey'


@app.route('/')
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


@app.route('/form_sample', methods=['POST', 'GET'])
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
            image.save(app.config['UPLOAD_FOLDER'] + "/image.png")
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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
