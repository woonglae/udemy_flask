from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h>'

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name)

@app.route('/<name>')
def debugEx(name):
    return "<h1>100th Letter {}</h1>".format(name[100])

@app.route('/puppy_latin/<name>')
def exercise(name):
    if (name[-1] != 'y'):
        name += 'y'
    else:
        name = name[:-1] + 'iful'

    return name


if __name__ == '__main__':
    app.run(debug=True)
