# using Bcrypt
#
# from flask_bcrypt import Bcrypt
#
# bcrypt = Bcrypt()
#
# password = 'supersecretpassword'
#
# hashed_password = bcrypt.generate_password_hash(password)
#
# print(hashed_password)
#
# check = bcrypt.check_password_hash(hashed_password,'supersecretpassword')
# print(check)


# using Werkzeug

from werkzeug.security import generate_password_hash,check_password_hash

hashed_password = generate_password_hash('mypassword')

print(hashed_password)

check = check_password_hash(hashed_password, 'wrong')
print(check)

check = check_password_hash(hashed_password, 'mypassword')
print(check)
