from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory data storage
users = []
swaps = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        data = request.form
        user = {
            'name': data.get('name', ''),
            'location': data.get('location', ''),
            'profile_photo': data.get('profile_photo', ''),
            'skills_offered': data.getlist('skills_offered'),
            'skills_wanted': data.getlist('skills_wanted'),
            'availability': data.get('availability', ''),
            'public_profile': data.get('public_profile', 'on') == 'on'
        }
        users.append(user)
        return render_template('index.html', message='User registered successfully!')
    return render_template('register.html')

@app.route('/users', methods=['GET'])
def list_users():
    return render_template('users.html', users=users)

@app.route('/request_swap', methods=['POST'])
def request_swap():
    data = request.get_json()

    # ✅ Check if JSON is missing
    if not data:
        return jsonify({'error': 'No JSON data received'}), 400

    required_fields = ['from_user', 'to_user', 'skill_offered', 'skill_requested']

    # ✅ Check if required fields exist
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # ✅ Safely extract fields
    swap_request = {
        'from_user': data.get('from_user'),
        'to_user': data.get('to_user'),
        'skill_offered': data.get('skill_offered'),
        'skill_requested': data.get('skill_requested')
    }

    swaps.append(swap_request)
    return jsonify({'message': 'Swap request sent!'}), 201

if __name__ == '_main_':
    app.run(debug=True,port=5001)
