from ex_db_1 import db, Puppy

# Creating
my_puppy = Puppy('Alissa', 5)
db.session.add(my_puppy)
db.session.commit()

# Reading
all_puppies = Puppy.query.all() #list of puppy objects in the tables
print(all_puppies)

# slecting
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# filtering
# Produce some sql code!!
puppy_franky = Puppy.query.filter_by(name='Ray')
print(puppy_franky.all()) # print in __repr__ form

# updating
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

#deleting
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

# all_puppies = Puppy.query.all()
print(all_puppies)
