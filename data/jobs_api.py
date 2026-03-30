import flask
from flask import jsonify, make_response, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                    'id', 'job', 'work_size', 'collaborators', 'speciality', 'is_finished', 'leader.name',
                    'leader.surname', "category.title"))
                    for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.get(Jobs, jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'id', 'job', 'work_size', 'collaborators', 'speciality', 'is_finished', 'leader.name',
                'leader.surname', "category.title"))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['job', 'work_size', 'collaborators', 'speciality', 'is_finished', 'team_leader', 'category_id']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        speciality=request.json['speciality'],
        is_finished=request.json['is_finished'],
        team_leader=request.json['team_leader'],
        category_id=request.json['category_id']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'id': jobs.id})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def edit_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.get(Jobs, jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    if "job" in request.json: jobs.job = request.json["job"]
    if "work_size" in request.json: jobs.work_size = request.json["work_size"]
    if "collaborators" in request.json: jobs.collaborators = request.json["collaborators"]
    if "speciality" in request.json: jobs.speciality = request.json["speciality"]
    if "is_finished" in request.json: jobs.is_finished = request.json["is_finished"]
    if "team_leader" in request.json: jobs.team_leader = request.json["team_leader"]
    if "category_id" in request.json: jobs.category_id = request.json["category_id"]
    db_sess.commit()
    return jsonify({'id': jobs.id})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.get(Jobs, jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})
