from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departament import Department
from data.categories import Categories

def add_new_info():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    session.query(Categories).delete()
    session.commit()
    names = ["Ridley", "James", "Yuriy", "Sergey"]
    surnames = ["Scott", "Cameron", "Gagarin", "Petkin"]
    ages = [21, 42, 27, 67]
    positions = ["captain", "colonist", "colonist", "colonist"]
    specialites = ["research engineer", "pilot", "pilot", "research engineer"]
    emails = ["scott_chief@mars.org", "jamesCameron@mars.org", "GagarinYura@mars.org", "SergPet@mars.org"]
    passwords = ["aaa", "bbb", "ccc", "ddd"]
    emails_was = [us.email for us in session.query(User).all()]
    for us in range(len(names)):
        if emails[us] not in emails_was:
            user = User()
            user.surname = surnames[us]
            user.name = names[us]
            user.age = ages[us]
            user.position = positions[us]
            user.speciality = specialites[us]
            user.address = f"module{us + 1}"
            user.email = emails[us]
            user.set_password(passwords[us])
            session.add(user)
    titles = ["engineering work", "technical work", "mental work", "rest"]
    for cat in range(len(titles)):
        category = Categories()
        category.title = titles[cat]
        session.add(category)
    leaders = [1, 2, 3]
    jobs = ["deployment of residential modules 1 and 2", "Patch up the crack in the ship", "Get enough sleep"]
    work_sizes = [15, 35, 10]
    collabs = ["2, 3", "1, 2", "One in a team"]
    categories = [2, 1, 4]
    finished = [False, True, True]
    for j in range(len(leaders)):
        jb = Jobs()
        jb.team_leader = leaders[j]
        jb.job = jobs[j]
        jb.work_size = work_sizes[j]
        jb.collaborators = collabs[j]
        jb.is_finished = finished[j]
        jb.category_id = categories[j]
        if jb.job not in [j.job for j in session.query(Jobs).all()]:
            session.add(jb)
    titles = ["dep1", "dep2"]
    collabs = ["2, 3", "1"]
    chiefs = [2, 1]
    emails = ["dep1@mars.org", "dep2@mars.org"]
    emails_was = [dep.email for dep in session.query(Department).all()]
    for dep in range(len(chiefs)):
        if emails[dep] not in emails_was:
            depart = Department()
            depart.title = titles[dep]
            depart.members = collabs[dep]
            depart.email = emails[dep]
            depart.chief = chiefs[dep]
            session.add(depart)
    session.commit()