from data.db_session import global_init, create_session
from data.jobs import Jobs
from data.users import User
from data.departament import Department

base = input()
global_init(base)
session = create_session()
users_id = [int(i) for i in session.query(Department).filter(Department.id == 1).first().members.split(", ")]
users = session.query(User).filter(User.id.in_(users_id)).all()
for us in users:
    hours = sum([j.work_size for j in session.query(Jobs).all() if str(us.id) in j.collaborators])
    if hours >= 25:
        print(us.surname, us.name)
