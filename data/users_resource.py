from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify, request
from data import db_session
from data.parser_users import parser
from data.users import User


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.get(User, user_id)
        return jsonify({'user': user.to_dict(
            only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.get(User, user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.get(User, user_id)
        users_email = [us.email for us in db_sess.query(User).all() if us.id != user_id]
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


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'city_from')) for item
            in
            users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            city_from=args['city_from']
        )
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})
