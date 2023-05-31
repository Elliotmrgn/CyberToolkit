from flask import Flask, render_template, request
from robotscan import getDenies

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}!'


@app.route('/robotscan', methods=['POST'])
def robot_scan():
    robotsite = request.form.get('robotsite')
    denies = getDenies(robotsite)
    return denies


if __name__ == '__main__':
    app.run(debug=True)
