from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'
# nao estou usando a porta 81 como no tutorial pois no linux para uso de portas pequeno preciso de permissao de adm (sudo) e tava dando uns problemas
app.run(host='0.0.0.0', port=5000)