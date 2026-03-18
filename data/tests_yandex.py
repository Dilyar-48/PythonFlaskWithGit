from data.db_session import global_init, create_session
from data.jobs import Jobs
from data.users import User

base = input()
global_init(base)
session = create_session()
for user in session.query(User).filter(User.address == "module_1", User.age < 21).all():
    user.address = "module_3"
session.commit()

