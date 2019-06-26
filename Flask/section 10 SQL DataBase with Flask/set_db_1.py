from ex_db_1 import db, Puppy

#Create all the tables model -> db table
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Franky',4)


print (sam.id)
print (frank.id)


## Add them all with list
db.session.add_all([sam,frank])

## or
## db.session.add(sam) & db.session.add(frank)
## to add them individually

db.session.commit()
