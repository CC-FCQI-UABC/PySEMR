from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import psycopg2
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuración de la conexión a PostgreSQL
def get_db_connection():
    connection = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    return connection

# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Establecer conexión con la base de datos
    conn = get_db_connection()
    cur = conn.cursor()

    # Consultar si el usuario existe en la base de datos
    cur.execute('SELECT password FROM users WHERE username = %s', (username,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        # Comparar la contraseña
        stored_password = result[0]
        if stored_password == password:
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Contraseña incorrecta"}), 401
    else:
        return jsonify({"message": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
