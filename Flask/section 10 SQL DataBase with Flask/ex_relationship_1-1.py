#Create entries into the tables

from ex_relationship_1 import db, Puppy, Owner, Toy

# create 2 puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add pippies to DB

db.session.add_all([rufus,fido])
db.session.commit()

# Check!
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Create owner object

jose = Owner('Jose', rufus.id)

# Give Rufus some report_toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# Grab Rufus after those addition

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
print(rufus.report_toys())
