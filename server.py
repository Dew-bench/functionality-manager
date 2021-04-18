from flask import Flask, request
import socket
import json
import requests

app = Flask(__name__)

DEVICES = {}
PIPES = {}
DEPLOYMENTS = {}
BROKERS = {}
SERVICE = {}


def create_proxy_for_device():
    pass

def create_proxy_for_service():
    pass

def ask_broker_for_service(service_id, depl_name):
    if len(BROKERS) != 0:
        url = BROKERS[BROKERS.keys()[0]]['url']
        try:
            response = requests.put(url, data=json.dumps({'id':service_id, 'depl':DEPLOYMENTS[depl_name]}), headers={"Content-Type": "application/json"})
        except requests.exceptions.RequestException as e:
            print(e)



######################################

@app.route('/')
def hello_world():
    return 'Dew service manager'

@app.route('/api/ip')
def get_ip():
    h_name = socket.gethostname()
    IP_addres = socket.gethostbyname(h_name)
    return json.dumps({
        "host_name": h_name,
        "ip": IP_addres
    })

######################################

@app.route('/api/pipeline/add/device', methods=['POST', 'PUT'])
def add_device():
    data = request.get_json() 
    DEVICES[data['id']] = data 
    return "ok"

@app.route('/api/pipeline/remove/device', methods=['POST', 'PUT'])
def remove_device():
    data = request.get_json() 
    DEVICES.pop(data['id'])
    return "ok"

@app.route('/api/pipeline/list/device', methods=['GET'])
def list_device():
    return json.dumps(DEVICES)

######################################

@app.route('/api/pipeline/add/pipe', methods=['POST', 'PUT'])
def add_pipe():
    data = request.get_json() 
    PIPES[data['name']] = data 
    return "ok"

@app.route('/api/pipeline/remove/pipe', methods=['POST', 'PUT'])
def remove_pipe():
    data = request.get_json() 
    PIPES.pop(data['name'])
    return "ok"

@app.route('/api/pipeline/list/pipe', methods=['GET'])
def list_pipe():
    return json.dumps(PIPES)

######################################

@app.route('/api/pipeline/add/depl', methods=['POST', 'PUT'])
def add_depl():
    data = request.get_json() 
    DEPLOYMENTS[data['name']] = data 
    return "ok"

@app.route('/api/pipeline/remove/depl', methods=['POST', 'PUT'])
def remove_depl():
    data = request.get_json() 
    DEPLOYMENTS.pop(data['name'])
    return "ok"

@app.route('/api/pipeline/list/depl', methods=['GET'])
def list_depl():
    return json.dumps(DEPLOYMENTS)

######################################

@app.route('/api/pipeline/add/broker', methods=['POST', 'PUT'])
def add_broker():
    data = request.get_json()
    BROKERS[data['id']] = data
    return "ok"

@app.route('/api/pipeline/remove/broker', methods=['POST', 'PUT'])
def remove_broker():
    data = request.get_json()
    BROKERS.pop(data['id'])
    return "ok"

@app.route('/api/pipeline/list/broker', methods=['GET'])
def list_brokers():
    return json.dumps(BROKERS)

######################################


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)