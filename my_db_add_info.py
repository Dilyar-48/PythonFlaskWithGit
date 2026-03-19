from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departament import Department

def add_new_info():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    session.query(User).delete()
    session.query(Jobs).delete()
    session.query(Department).delete()
    session.commit()
    names = ["Ridley", "James", "Yuriy", "Sergey"]
    surnames = ["Scott", "Cameron", "Gagarin", "Petkin"]
    ages = [21, 42, 27, 67]
    positions = ["captain", "colonist", "colonist", "colonist"]
    specialites = ["research engineer", "pilot", "pilot", "research engineer"]
    emails = ["scott_chief@mars.org", "jamesCameron@mars.org", "GagarinYura@mars.org", "SergPet@mars.org"]
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
    leaders = [1, 2, 3]
    jobs = ["deployment of residential modules 1 and 2", "Patch up the crack in the ship", "Get enough sleep"]
    work_sizes = [15, 35, 10]
    collabs = ["2, 3", "1, 2", "One in a team"]
    finished = [False, True, True]
    for j in range(len(leaders)):
        jb = Jobs()
        jb.team_leader = leaders[j]
        jb.job = jobs[j]
        jb.work_size = work_sizes[j]
        jb.collaborators = collabs[j]
        jb.is_finished = finished[j]
        session.add(jb)
    titles = ["dep1", "dep2"]
    collabs = ["2, 3", "1"]
    chiefs = [2, 1]
    emails = ["dep1@mars.org", "dep2@mars.org"]
    for dep in range(len(chiefs)):
        depart = Department()
        depart.title = titles[dep]
        depart.members = collabs[dep]
        depart.email = emails[dep]
        depart.chief = chiefs[dep]
        session.add(depart)
    session.commit()