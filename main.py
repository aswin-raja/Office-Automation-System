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


admindata = {'stock@ucen': '123',
            'scholarship@ucen': 'scholarship@admin', }


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
            return render_template('bonafide.html')
         
    else:
       if admindata[name] == admindata['scholarship@ucen']:
            return render_template('scholarship.html')
        
mysql = MySQL()
 

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'bonafide'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def upload_form():
	return render_template('bonafide.html')

@app.route('/download/report/pdf')
def download_report():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(mysql.cursors.DictCursor)
		
		cursor.execute("SELECT regnumber, name, fathername, year FROM studentdata")
		result = cursor.fetchall()
		
		pdf = FPDF()
		pdf.add_page()
		
		page_width = pdf.w - 2 * pdf.l_margin
		
		pdf.set_font('Times','B',14.0) 
		pdf.cell(page_width, 0.0, 'Employee Data', align='C')
		pdf.ln(10)

		pdf.set_font('Courier', '', 12)
		
		col_width = page_width/4
		
		pdf.ln(1)
		
		th = pdf.font_size
		
		for row in result:
			pdf.cell(col_width, th, (row['regnumber']), border=1)
			pdf.cell(col_width, th, row['name'], border=1)
			pdf.cell(col_width, th, row['fathername'], border=1)
			pdf.cell(col_width, th, row['year'], border=1)
			pdf.ln(th)
		
		pdf.ln(10)
		
		pdf.set_font('Times','',10.0) 
		pdf.cell(page_width, 0.0, '- end of report -', align='C')
		return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition':'attachment; filename=employee_report.pdf'})
	except Exception as e:
		print(e)
	finally:
		conn.close()


if __name__ == '__main__':
    app.run(debug=True)
