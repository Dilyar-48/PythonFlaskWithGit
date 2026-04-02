import flask
from flask import jsonify, make_response, request, render_template
from flask_login import login_required
import requests
import sys
from ymaps import Static

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


def spn_sizes(s):
    toponym_size_w = abs(
        float(s["lowerCorner"].split()[0]) - float(s["upperCorner"].split()[0]))
    toponym_size_h = abs(
        float(s["lowerCorner"].split()[1]) - float(s["upperCorner"].split()[1]))
    max_coord = min(toponym_size_w, toponym_size_h)
    return str(round(max_coord, int(str(max_coord).count("0") + 1)))


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=(
                    'id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from')) for item
                    in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'user': user.to_dict(only=(
                'id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', "hashed_password",
                  "city_from"]):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    users = [us.email for us in db_sess.query(User).all()]
    if request.json['email'] in users:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    user = User(
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        city_from=request.json['city_from'],
        hashed_password=hash(request.json['hashed_password'])
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'id': user.id})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    users_email = [us.email for us in db_sess.query(User).all() if us.id != user_id]
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    if "surname" in request.json: user.surname = request.json["surname"]
    if "name" in request.json: user.name = request.json["name"]
    if "age" in request.json: user.age = request.json["age"]
    if "position" in request.json: user.position = request.json["position"]
    if "speciality" in request.json: user.speciality = request.json["speciality"]
    if "address" in request.json: user.address = request.json["address"]
    if "hashed_password" in request.json: user.hashed_password = request.json["hashed_password"]
    if "city_from" in request.json: user.city_from = request.json["city_from"]
    if "email" in request.json and request.json["email"] not in users_email: user.email = request.json["email"]

    db_sess.commit()
    return jsonify({'id': user.id})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/users_show/<int:user_id>', methods=['GET'])
@login_required
def user_show(user_id):
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    user_city = user.city_from
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": user_city,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_coodrinates = [float(n) for n in toponym["Point"]["pos"].split(" ")]
        spn = float(spn_sizes(toponym["boundedBy"]["Envelope"]))
        response = Static(url='1.x').get_image(ll=toponym_coodrinates, spn=[spn, spn], l=["sat"])
        with open('./static/img/map.png', "wb") as f:
            f.write(response)
        return render_template("user_show.html", user=user)
