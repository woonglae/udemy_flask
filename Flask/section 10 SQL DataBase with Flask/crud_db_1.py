from ex_db_1 import db, Puppy

my_puppy = Puppy('Ray', 5)
db.session.add(my_puppy)
db.session.commit()
