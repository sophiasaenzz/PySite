from flask import Flask
from flask import render_template, Request

app = Flask(__name__)

# Function to read in details for page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]


@app.route("/")
def homePage():
    name = "Sophia Saenz"
    details = readDetails('static/details.txt')
    return render_template('base.html', name = name, aboutMe = details)


@app.route("/user/<name>")
def greet(name):
    return f'<p>Hello, {name}!</p>'


@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name= request.form['name']

    return render_template('form.html', name=name)

#if __name__ == '__main__':
    #app.run(debug=True)
