from flask import Flask, jsonify
from sqlalchemy import create_engine, text

# Initialize the Flask application
app = Flask(__name__)

DB_USER = 'master'
DB_PASSWORD = 'elkomba2'
DB_HOST = 'database-1.cpgwsuckign8.us-east-2.rds.amazonaws.com'
DB_NAME = 'domicilios_tijuana'
DB_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DB_URI)

@app.route('/data')
def obtener_data():
    try:
        
        with engine.connect() as connection:
            
            query = text('SELECT * FROM domicilios LIMIT 10')

            resultados = connection.execute(query)
            
            data = []
            column_names = list(resultados.keys())
            for row in resultados:
                data_dict = {}
                for i in range(len(row)):
                    data_dict[column_names[i]] = row[i]
                data.append(data_dict)

            return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
