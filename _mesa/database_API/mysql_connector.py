import boto3
import os  # Agregar esta línea
from flask import Flask, jsonify
from sqlalchemy import create_engine, text

# Establecer la región de AWS en la variable de entorno
os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'

# Initialize the Flask application
app = Flask(__name__)

# Tu configuración de base de datos existente
DB_USER = 'master'
DB_PASSWORD = 'elkomba2'
DB_HOST = 'database-1.cpgwsuckign8.us-east-2.rds.amazonaws.com'
DB_NAME = 'domicilios_tijuana'
DB_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DB_URI)

# Crear un cliente de AWS Lambda
lambda_client = boto3.client('lambda')

# Definir los ARN de las funciones Lambda
ENCENDER_INSTANCIA_RDS_ARN = 'arn:aws:lambda:us-east-2:162485998614:function:encender_instancia_rds'
APAGAR_INSTANCIA_ARN = 'arn:aws:lambda:us-east-2:162485998614:function:apagar_instancia'

# Función para invocar la función Lambda especificada
def invoke_lambda_function(lambda_arn):
    try:
        response = lambda_client.invoke(
            FunctionName=lambda_arn,
            InvocationType='Event'
        )
        return f"Lambda function {lambda_arn} invoked successfully"
    except Exception as e:
        raise e

# Función para recuperar datos de la base de datos
def retrieve_data():
    try:
        with engine.connect() as connection:
            query = text('SELECT * FROM domicilios LIMIT 50000')
            resultados = connection.execute(query)
            
            data = []
            column_names = list(resultados.keys())
            for row in resultados:
                data_dict = {}
                for i in range(len(row)):
                    data_dict[column_names[i]] = row[i]
                data.append(data_dict)
                
            return data
    except Exception as e:
        raise e

@app.route('/data')
def obtener_data():
    try:
        # Llamar a la función Lambda para iniciar la instancia de RDS
        invoke_lambda_function(ENCENDER_INSTANCIA_RDS_ARN)
        print("Instancia encendida!")
        # Recuperar datos de la base de datos
        data = retrieve_data()
        
        # Llamar a la función Lambda para detener la instancia de RDS
        invoke_lambda_function(APAGAR_INSTANCIA_ARN)
        print("Instancia apagada!")
        
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
