from flask import Flask, jsonify, request

app = Flask(__name__)

agents = []


@app.route('/agent/<string:name>')
def get_agent(name):
    for agent in agents:
        if agent['name'] == name:
            return jsonify(agent['name'])
    return jsonify({'message': 'Agent not found'})


@app.route('/agent/<string:name>/detail')
def get_agent_item(name):
    for agent in agents:
        if agent['name'] == name:
            return jsonify(agent['details'])
    return jsonify({'message': 'Agent not found'})


@app.route('/agent', methods=['POST'])
def create_agent():
    req_data = request.get_json()
    new_agent = {
        'name': req_data['name'],
        'details': req_data['details']
    }
    agents.append(new_agent)
    return jsonify(new_agent)


@app.route('/agent/<string:name>/detail', methods=['POST'])
def create_agent_detail(name):
    for agent in agents:
        if agent['name'] == name:
            req_data = request.get_json()
            new_detail = {
                'age': req_data['age'],
                'surname': req_data['surname'],
                'dob': req_data['dob']

            }
            agent['detail'].append(new_detail)
            return jsonify(new_detail)
        return jsonify({'message': 'Agent not found'})


@app.route('/')
def home():
    return "hey"


app.run(port=8000)
