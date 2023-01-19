from flask import Flask, render_template, jsonify, request
import traceback
from base import insertP, insertC, sessionmaker, engine
from sqlalchemy.sql import func

app = Flask(__name__, static_folder='staticFiles', template_folder='templates')

Session = sessionmaker(bind=engine)

@app.route("/")
def index():
    try:
        return render_template('index.html')
    except:
        return jsonify({'trace': traceback.format_exc()}) 

"""
Function /register - email/username/password

@app.route("/register")
def register():
"""

@app.route("/postulante")
def postulante():
    try:
        return render_template('postulante.html')
    except:
        return print('error')

@app.route("/cliente")
def cliente():
    try:
        return render_template('cliente.html')
    except:
        return print('error')

#Insert data postulante
@app.route("/nuevoPos", methods=['GET','POST'])
def nuevoPos():
    if request.method == 'POST':
        n = str(request.form.get('name')).capitalize()#amount
        l = str(request.form.get('lastName')).capitalize()#description     
        e = str(request.form.get('email'))
        insertP(n, l, e)

        print('DATO SUBIDO (POSTULANTE)')
        return render_template('postulante.html')
    else:
        print('ERROR')
        return jsonify({'trace': traceback.format_exc()})

#Insert data cliente
@app.route("/nuevoCli", methods=['GET','POST'])
def nuevoCli():
    if request.method == 'POST':            ##    CLIENT
        c = str(request.form.get('company')).capitalize()#company
        r = str(request.form.get('representative')).capitalize()#name representate
        e = str(request.form.get('email'))
        p = request.form.get('phone')#phone number
        insertC(c, r, e, p)

        print('DATO SUBIDO (CLIENTE)')
        return render_template('cliente.html')
    else:
        print('ERROR')
        return jsonify({'trace': traceback.format_exc()})



if __name__ == '__main__':
    app.run(debug=True)