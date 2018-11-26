from flask import Flask, render_template
from flask import render_template, request, flash
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def site():
    return render_template('site.html')

@app.route('/planos')
def planos():
#    return render_template('planos.html')
    return render_template('preco.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/sis')
def sis():
    return render_template('layoutsis.html')


@app.route('/login',methods=['GET','POST'])
def login():
    erro = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            erro = 'Usuario invalido!'
        elif request.form['password'] != app.config['PASSWORD']:
            pass
    return render_template('login.html')


@app.route('/cadempresa')
def cadempresa():
    return render_template('cadempresa.html')



if __name__ == '__main__':
        app.run(host='127.0.0.1', port='5001', debug=True)

