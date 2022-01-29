from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    users = ['Rosalia', 'Adrianna', 'Victoria']
    return render_template('index.html', title='Welcome', members=users)


# nao estou usando a porta 81 como no tutorial pois no linux para uso de portas pequeno preciso de permissao de adm (sudo) e tava dando uns problemas
app.run(host='0.0.0.0', port=5000)
