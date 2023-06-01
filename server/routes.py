from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from routes.robotscan.robotscan import getDenies
from routes.portscan.portscan import port_check

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/api/robotscan', methods=['POST'])
def robot_scan():
    robotsite = request.json.get('robotsite')
    denies = getDenies(robotsite)
    return denies

@app.route('/api/portscan', methods=['POST'])
def port_scan():
    data = request.json
    host = data['host']
    start_port = data['start_port']
    stop_port = data['stop_port']
    
    open_ports = port_check(host, start_port, stop_port)

    return open_ports
    


if __name__ == '__main__':
    app.run(debug=True)
