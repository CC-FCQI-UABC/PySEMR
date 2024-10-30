from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine, text

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

DB_USER = 'openemr'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_NAME = 'emr_datasets'
DB_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DB_URI)

def query_to_dict_list(results, dataset_list):
    columns = list(results.keys())
    for row in results:
        data_dict = {}
        for i in range(len(row)):
            data_dict[columns[i]] = row[i]
        dataset_list.append(data_dict)   

@app.route('/login', methods=['POST'])
def login():
    try:
        # Get username and password from the request body (JSON)
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        print(f"Username: {username}, Password: {password}")  # Debug print
        
        if not username or not password:
            return jsonify({"message": "Username and password are required."}), 400
        
        with engine.connect() as connection:
            # Query to check if the user exists and the password matches
            query_login = text("SELECT * FROM users WHERE username = :username AND password = :password")
            user = connection.execute(query_login, {"username": username, "password": password}).fetchone()

            if user:
                return jsonify({"message": "Login successful"}), 200
            else:
                return jsonify({"message": "Invalid username or password"}), 401
    except Exception as e:
        print(f"Error: {e}")  # Debug print
        return jsonify({"error": str(e)}), 500

@app.route('/data')
def obtener_data():
    try:
        with engine.connect() as connection:
            query_address = text('SELECT * FROM address limit 50000;')
            query_female_names = text('SELECT * FROM female_names;')
            query_male_names = text('SELECT * FROM male_names;')
            query_last_names = text('SELECT * FROM apellidos;')

            address_results = connection.execute(query_address)
            female_names_results = connection.execute(query_female_names)
            male_names_results = connection.execute(query_male_names)
            last_names_results = connection.execute(query_last_names)

            data = {
                "Address": [],
                "FemaleNames": [],
                "MaleNames": [],
                "LastNames": []
            }

            query_to_dict_list(address_results, data["Address"])
            query_to_dict_list(female_names_results, data["FemaleNames"])
            query_to_dict_list(male_names_results, data["MaleNames"])
            query_to_dict_list(last_names_results, data["LastNames"])

            return jsonify({"status": "success", "data": data})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    
@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users."""
    try:
        with engine.connect() as connection:
            query = text("SELECT * FROM users")
            results = connection.execute(query)
            users = []
            query_to_dict_list(results, users)
            return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"message": "Username and password are required."}), 400

        # Begin a transaction
        with engine.begin() as connection:  # This ensures that the transaction is committed
            query = text("INSERT INTO users (username, password) VALUES (:username, :password)")
            connection.execute(query, {"username": username, "password": password})
            
        return jsonify({"message": "User created successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users/<string:username>', methods=['DELETE'])
def delete_user(username):
    """Delete a user by username."""
    try:
        with engine.begin() as connection:
            query = text("DELETE FROM users WHERE username = :username")
            result = connection.execute(query, {"username": username})
            if result.rowcount == 0:
                return jsonify({"message": "User not found."}), 404
            return jsonify({"message": "User deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)