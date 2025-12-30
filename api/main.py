import logging
import os
from flask import Flask, request, jsonify
from api_service.config import Config
from api_service.routes import api_blueprint

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api_blueprint)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)