import mysql.connector
import jinja2
import pdfkit
from fpdf import FPDF
from flaskext.mysql import MySQL
from werkzeug.wrappers import Request, Response
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
@app.route('/stockadmin')
def stockadmin():
    return render_template("stockadmin.html")


admindata = {'stock@ucen': '123',
            'scholarship@ucen': '123', }


@app.route('/form_login', methods=['POST', 'GET'])
def login():
    name = request.form['adminusername']
    pwd = request.form['adminpassword']
    if name not in admindata:
        return render_template('login.html',
                               info='Invalid User !')
    
    elif admindata[name] != pwd:
         return render_template('login.html',
                                   info='Invalid Password !')
            
    elif admindata[name] == admindata['stock@ucen']:
            return render_template('stock.html')
         
    else:
       if admindata[name] == admindata['scholarship@ucen']:
            return render_template('scholarship.html')
        
if __name__ == '__main__':
    app.run(debug=True)
