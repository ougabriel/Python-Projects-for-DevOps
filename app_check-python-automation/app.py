from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message = 'Hello Gabriel') 

@app.route('/health')
def healthz_check():
    return jsonify(status = 'UP')

@app.route('/config')
def config():
    config_settings = {
        "version": '1.0.10',
        "Environment": 'Testing',
        "Debug": False
    }
    return jsonify(config_settings)

if __name__ == '__main__':
 app.run(host = '0.0.0.0', port = 3000)