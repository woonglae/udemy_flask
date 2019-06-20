from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Ray"
    mylist = [1,2,3,4,5]
    return render_template('ex_templates_1.html', name=name, mylist = mylist)

if __name__ == '__main__':
    app.run(debug=True)
