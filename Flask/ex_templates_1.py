from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Ray"
    letters = list(name)
    dictionary = {"name":'Ray'}
    return render_template('ex_templates_1.html', name=name, letters=letters, dictionary=dictionary)

if __name__ == '__main__':
    app.run(debug=True)
