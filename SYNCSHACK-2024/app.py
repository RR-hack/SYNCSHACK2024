from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Path to the JSON file
json_file_path = 'users.json'

# Ensure the JSON file exists
if not os.path.exists(json_file_path):
    with open(json_file_path, 'w') as f:
        json.dump({"users": []}, f)

@app.route('/save', methods=['POST'])
def save_data():
    # Get JSON data from the request
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    hobbies = data.get('hobbies', [])  # Get hobbies if provided, otherwise use an empty list

    print(username)

    # Load existing data
    with open(json_file_path, 'r') as f:
        users_data = json.load(f)

    # Add new user data
    users_data['users'].append({'username': username, 'password': password, 'hobbies': hobbies})

    # Save data back to the JSON file
    with open(json_file_path, 'w') as f:
        json.dump(users_data, f, indent=2)

    return jsonify({'message': 'User saved successfully!'}), 200

@app.route('/save_hobbies', methods=['POST'])
def save_hobbies():
    # Get JSON data from the request
    data = request.get_json()

    industries = data.get('industries')
    hobbies = data.get('hobbies')

    # Load existing data
    with open(json_file_path, 'r') as f:
        users_data = json.load(f)

    # Update hobbies for the last user
    if users_data['users']:
        users_data['users'][-1]['industries'] = industries
        users_data['users'][-1]['hobbies'] = hobbies

    # Save data back to the JSON file
    with open(json_file_path, 'w') as f:
        json.dump(users_data, f, indent=2)

    return jsonify({'message': 'Hobbies saved successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
