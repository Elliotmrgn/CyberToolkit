from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from routes.robotscan import getDenies

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/robotscan', methods=['POST'])
def robot_scan():
    robotsite = request.json.get('robotsite')
    print(f"\n********\n{robotsite}\n\n\n")
    denies = getDenies(robotsite)
    return denies


if __name__ == '__main__':
    app.run(debug=True)
