from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def page_first():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


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
                    <h4>Человечество вырастает из детства.</h2>
                    <h4 style='color: green;'>Человечеству мала одна планета.</h2>
                    <h4 style='color: blue;'>Мы сделаем обитаемыми безжизненные пока планеты.</h2>
                    <h4>И начнем с Марса!</h2>
                    <h4 style='color: #7B68EE;'>Присоединяйся!</h2>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')