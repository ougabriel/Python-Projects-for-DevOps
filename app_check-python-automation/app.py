from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
 return 'Hello Gabriel'

@app.route('/greet')
def greet():
   name = request.args.get('name', 'Guest') 
   return f"Hello, {name}" 

@app.route('/health')
def healthz_check():
    return  'UP'

@app.route('/config')
def config():
    config_settings = {
        "version": '1.0.10',
        "Environment": 'Testing',
        "Debug": False
    }
    return "/n".join(f"{key}:{value}" for key, value in config_settings.items())

if __name__ == '__main__':
 app.run(host = '0.0.0.0', port = 3000)