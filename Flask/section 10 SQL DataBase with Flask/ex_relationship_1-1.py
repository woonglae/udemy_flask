#Create entries into the tables

from models import db, Puppy, Owner, Toy

# create 2 puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add pippies to DB

db.session.add_all([rufus,fido])
db.session.commit()

# Check!
print(Puppy.query.all())
