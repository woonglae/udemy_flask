from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


# This page will be the page after the form
@app.route('/report')
def report():
    username = request.args.get('username')

    lower = False
    upper = False
    number = False

    if (any(item.islower() for item in username)):
        lower=True
    if (any(item.isupper() for item in username)):
        upper=True
    if (username[-1].isdigit()):
        number=True
    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    return render_template('ty1.html', username=username, lower=lower, upper=upper, number=number)

if __name__ == '__main__':
    app.run(debug=True)
