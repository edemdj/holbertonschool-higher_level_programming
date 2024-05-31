from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt_claims
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for JWT
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a strong secret key in production
jwt = JWTManager(app)

# Sample user data
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpassword"), "role": "admin"}
}

# Basic HTTP authentication
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username).get('password'), password):
        return username

# JWT token generation
def generate_token(username):
    access_token = create_access_token(identity=username)
    return access_token

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    user = users.get(username)
    if not user or not check_password_hash(user.get('password'), password):
        return jsonify({"message": "Invalid username or password"}), 401
    access_token = generate_token(username)
    return jsonify({"access_token": access_token}), 200

# Protected route with Basic authentication
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

# Protected route with JWT authentication
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"}), 200

# Role-based protected route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    claims = get_jwt_claims()
    if claims['role'] != 'admin':
        return jsonify({"message": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
