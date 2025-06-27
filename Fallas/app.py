from flask import Flask, jsonify, request
import logging

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración del sistema de logging
logging.basicConfig(
    level=logging.INFO,  # Configurar el nivel de logging (INFO, DEBUG, ERROR, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Definir el formato de los logs
    handlers=[logging.FileHandler('app.log'), logging.StreamHandler()]  # Guardar logs en archivo y en consola
)

# Crear un logger para capturar los logs
logger = logging.getLogger(__name__)

# Listas para llevar un registro de los errores
error_log = []
error_stats = {'400_BAD_REQUEST': 0, '404_NOT_FOUND': 0, '500_INTERNAL_ERROR': 0}

# Manejo de errores
@app.errorhandler(400)
def bad_request_error(error):
    error_stats['400_BAD_REQUEST'] += 1
    error_log.append('400: JSON vacío o malformado')
    logger.error("400 Bad Request: JSON vacío o malformado")  # Log del error
    return jsonify({"message": "Bad Request: JSON vacío o malformado"}), 400

@app.errorhandler(404)
def not_found_error(error):
    error_stats['404_NOT_FOUND'] += 1
    error_log.append('404: Recurso no encontrado')
    logger.error("404 Not Found: Recurso no encontrado")  # Log del error
    return jsonify({"message": "Not Found: Recurso no encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    error_stats['500_INTERNAL_ERROR'] += 1
    error_log.append('500: Error interno del servidor')
    logger.error("500 Internal Error: Errores internos del servidor")  # Log del error
    return jsonify({"message": "Internal Server Error: Errores internos del servidor"}), 500

# API para ver las estadísticas de los errores
@app.route('/errors/stats')
def error_stats_view():
    return jsonify({
        'total_errors': sum(error_stats.values()),
        'error_types': dict(error_stats),
        'recent_errors': error_log[-10:]
    })

# Endpoint para simular errores (simulación correcta de los errores)
@app.route('/cause_error/<error_type>')
def cause_error(error_type):
    if error_type == "400":
        return jsonify({"message": "Bad Request: JSON vacío o malformado"}), 400
    elif error_type == "404":
        return jsonify({"message": "Not Found: Recurso no encontrado"}), 404
    elif error_type == "500":
        return jsonify({"message": "Internal Server Error: Errores internos del servidor"}), 500
    return "No Error"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
