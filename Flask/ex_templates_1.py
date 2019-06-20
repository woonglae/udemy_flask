from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    some_variable = "Ray"
    return render_template('ex_templates_1.html', my_variable = some_variable)

if __name__ == '__main__':
    app.run(debug=True)
