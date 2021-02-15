from flask import Flask, jsonify, request, abort, json


api = [{'id': 0, 'header': 'current temperature', 'value': 0},
       {'id': 1, 'header': 'current lighting', 'value': 0},
       {'id': 2, 'header': 'reference temperature', 'value': 0},
       {'id': 3, 'header': 'reference lighting', 'value': 0},
       {'id': 4, 'header': 'manual heater control', 'value': False},
       {'id': 5, 'header': 'manual heater value', 'value': 0},
       {'id': 6, 'header': 'manual blind control', 'value': False},
       {'id': 7, 'header': 'manual height value', 'value': 0},
       {'id': 8, 'header': 'manual tilt value', 'value': 0}]


app = Flask(__name__)


# To get api in web browser type in http://localhost:105/dorn/all
@app.route('/dorn/all', methods=['GET'])
def api_all():
    return jsonify(api)


# To get id=0 in web browser type in http://localhost:105/dorn/id?=0
@app.route('/dorn/<int:id>', methods=['GET','PUT'])
def api_get(id):
    if request.method == 'GET':
        results = []
        for data in api:
            if data['id'] == id:
                results.append(data)
        if len(results) == 0:
            abort(404)
        return jsonify(results)
    elif request.method == 'PUT':
        new_value = json.loads(request.get_json())
        for i, data in enumerate(api):
            if data['id'] == id:
                api[i]['value'] = new_value['value']
                return jsonify(api[i])
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)