from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def fn_get_users():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['POST'])
def fn_post_user():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['DELETE'])
def fn_delete_user():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['PUT'])
def fn_put_user():
    return jsonify({'payload': 'success', "error": False})

@app.route('/api/v1/users', methods=['GET'])
def fn_api_get_users():
    return jsonify({
        "payload":[]})

@app.route('/api/v1/user', methods=['POST'])
def fn_post_api_user():
    email = request.args.get('email')
    name = request.args.get('name')
    response = {
        'payload': {
            'email': email,
            'name': name
        }
    }
    
    return jsonify(response)

@app.route('/api/v1/user/add', methods=['POST'])
def fn_add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    user_id = request.form.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': user_id
        }
    })

@app.route('/api/v1/user/create', methods=['POST'])
def fn_create_user():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    user_id = data.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': user_id
        }
    })

if __name__ == "__main__":
    app.run(debug=True)