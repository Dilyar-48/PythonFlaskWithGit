from flask_restful import reqparse, abort, Api, Resource
from flask import jsonify, request
from data import db_session
from data.parser_jobs import parser
from data.jobs import Jobs


def abort_if_user_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_user_not_found(job_id)
        session = db_session.create_session()
        job = session.get(Jobs, job_id)
        return jsonify({'user': job.to_dict(
            only=(
                'id', 'job', 'work_size', 'collaborators', 'speciality', 'is_finished', 'leader.name', 'leader.surname',
                'category.title'))})

    def delete(self, job_id):
        abort_if_user_not_found(job_id)
        session = db_session.create_session()
        job = session.get(Jobs, job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, job_id):
        abort_if_user_not_found(job_id)
        db_sess = db_session.create_session()
        job = db_sess.get(Jobs, job_id)

        if "job" in request.json: job.job = request.json["job"]
        if "work_size" in request.json: job.work_size = request.json["name"]
        if "collaborators" in request.json: job.collaborators = request.json["age"]
        if "speciality" in request.json: job.speciality = request.json["position"]
        if "is_finished" in request.json: job.is_finished = request.json["speciality"]
        if "team_leader" in request.json: job.team_leader = request.json["team_leader"]
        if "category_id" in request.json: job.category_id = request.json["category_id"]

        db_sess.commit()
        return jsonify({'id': job.id})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=(
                'id', 'job', 'work_size', 'collaborators', 'speciality', 'is_finished', 'leader.name', 'leader.surname',
                'category.title')) for item
            in
            jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            speciality=args['speciality'],
            is_finished=args['is_finished'],
            team_leader=args['team_leader'],
            category_id=args['category_id']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'id': jobs.id})
