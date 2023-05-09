from flask import Flask,render_template,request,session,redirect,url_for,flash, make_response, send_file
from flask_sqlalchemy import SQLAlchemy
from reportlab.lib.pagesizes import A4, portrait
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ucenofficeautomation'

#database Configuration
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/studentprofile'
db=SQLAlchemy(app)

#Table for studnt details
class student(db.Model):
    SI_NO = db.Column(db.Integer, primary_key=True)
    APPL_NO = db.Column(db.String(50))
    ROLL_NO = db.Column(db.Integer)
    NAME = db.Column(db.String(50)) 
    DOB_YYYY_MM_DD  = db.Column(db.String(50))  
    GENDER = db.Column(db.String(50))
    YEAR = db.Column(db.String(50)) 
    DEGREE = db.Column(db.String(50))
    BRANCH  = db.Column(db.String(50))
    MODE = db.Column(db.String(50)) 
    TYPE = db.Column(db.String(100))    
    BLOOD_GROUP = db.Column(db.String(100)) 
    NATIONALITY = db.Column(db.String(100)) 
    RELIGION = db.Column(db.String(100))    
    COMMUNITY   = db.Column(db.String(100)) 
    SUB_CASTE   = db.Column(db.String(100)) 
    PERSONAL_IDENTIFICATION = db.Column(db.String(100)) 
    ID_TYPE = db.Column(db.String(100)) 
    ID_NUMBER   = db.Column(db.String(100)) 
    MOTHER_LANGUAGE = db.Column(db.String(100)) 
    OTHER_LANGUAGE  = db.Column(db.String(100)) 
    HEIGHT  = db.Column(db.String(100)) 
    WEIGHT  = db.Column(db.String(100)) 
    ANY_ALIGNMENT   = db.Column(db.String(100)) 
    ALERGIC = db.Column(db.String(100)) 
    HOBBIES = db.Column(db.String(100)) 
    MOBILE  = db.Column(db.String(100)) 
    E_MAIL  = db.Column(db.String(100)) 
    PMS = db.Column(db.String(100)) 
    DA  = db.Column(db.String(100)) 
    FG  = db.Column(db.String(100)) 
    Column_10TH_REGISTER_NO = db.Column(db.String(100)) 
    Column_10TH_MARK = db.Column(db.String(100))    
    Column_10TH_OVERALLPERCENTAGE   = db.Column(db.String(100)) 
    Column_12TH_REGISTER_NO = db.Column(db.String(100)) 
    Column_12TH_MARK    = db.Column(db.String(100)) 
    Column_12TH_OVERALLPERCENTAGE   = db.Column(db.String(100)) 
    MATHS   = db.Column(db.String(100)) 
    PHYSICS = db.Column(db.String(100)) 
    CHEMISTRY   = db.Column(db.String(100)) 
    COUNCILING_CUTOFF   = db.Column(db.String(100)) 
    COUNCELING_RANK = db.Column(db.String(100)) 
    BOARD_OF_EXAM   = db.Column(db.String(100)) 
    SCHOOL_UNDER    = db.Column(db.String(100)) 
    SCHOOL_NAME = db.Column(db.String(100)) 
    MEDIUM  = db.Column(db.String(100)) 
    DIPLOMA_STATUS  = db.Column(db.String(100)) 
    DIPLOMA_IN  = db.Column(db.String(100)) 
    OVERALLPERCENTAGE   = db.Column(db.String(100)) 
    COLLEGE_NAME    = db.Column(db.String(100)) 
    UG_PG_STATUS    = db.Column(db.String(100)) 
    UG_PG   = db.Column(db.String(100)) 
    OVERALLPERCENTAGE_1 = db.Column(db.String(100)) 
    COLLEGE_NAME_1  = db.Column(db.String(100)) 
    EXTRA_CURRICULAR    = db.Column(db.String(100)) 
    ACHIVEMENT  = db.Column(db.String(100)) 
    HOSTEL_REQUIREMENT  = db.Column(db.String(100)) 
    FATHER_NAME = db.Column(db.String(100)) 
    FATHER_OCCUPATION   = db.Column(db.String(100)) 
    FATHER_MOBILE   = db.Column(db.String(100)) 
    FATHER_MAIL = db.Column(db.String(100)) 
    MOTHER_NAME = db.Column(db.String(100)) 
    MOTHER_OCCUPATION   = db.Column(db.String(100)) 
    MOTHER_MOBILE   = db.Column(db.String(100)) 
    MOTHER_MAIL = db.Column(db.String(100)) 
    PERMENANT_ADDRESS_1 = db.Column(db.String(100)) 
    PERMENANT_ADDRESS_2 = db.Column(db.String(100)) 
    DISTRICT    = db.Column(db.String(100)) 
    STATE   = db.Column(db.String(100)) 
    PINCODE = db.Column(db.String(100)) 
    COMMUNICATION_ADDRESS_1 = db.Column(db.String(100)) 
    COMMUNICATION_ADDRESS_2 = db.Column(db.String(100)) 
    DISTRICT_1  = db.Column(db.String(100)) 
    STATE_1 = db.Column(db.String(100)) 
    PINCODE_1   = db.Column(db.String(100)) 
    CATEGORY    = db.Column(db.String(100)) 
    GURDIAN = db.Column(db.String(100)) 
    MOBILE_1    = db.Column(db.String(100)) 
    GURD_ADDRESS_1  = db.Column(db.String(100)) 
    GURD_ADDRESS_2  = db.Column(db.String(100)) 
    DISTRICT_2  = db.Column(db.String(100)) 
    STATE_2 = db.Column(db.String(100)) 
    PINCODE_2   = db.Column(db.String(100)) 
    SIBILING_REGNO  = db.Column(db.String(100)) 
    RELATION_TYPE = db.Column(db.String(100)) 
    ANNUAL_INCOME   = db.Column(db.String(100)) 
    PROGRAMME   = db.Column(db.String(100)) 
    CAMPCODE    = db.Column(db.String(100)) 
    ADMISSION_DATE_YYYY_MM_DD   = db.Column(db.String(100))
    NO_OF_ARREARS = db.Column(db.Integer) 
    PLACEMENT_STATUS = db.Column(db.String(100))

class stock_management(db.Model):
    SI_NO = db.Column(db.Integer, primary_key=True)
    STOCK_TYPE = db.Column(db.String(100)) 
    DEPARTMENT = db.Column(db.String(100)) 
    PRODUCT_ID = db.Column(db.Integer)
    DATE_OF_PURCHASE = db.Column(db.String(100)) 
    BILL_INVOICE_NO = db.Column(db.String(100)) 
    BILL_DATE = db.Column(db.String(100)) 
    EQUIPMENT = db.Column(db.String(100)) 
    NO_OF_QUANTITY =  db.Column(db.Integer) 
    COST_PER_UNIT =  db.Column(db.Integer)  
    TOTAL_COST =  db.Column(db.Integer) 
    SUPPLIER_NAME  = db.Column(db.String(100)) 
    WARRANTY = db.Column(db.String(100)) 
    WARRANTY_PERIOD =db.Column(db.String(100)) 
    TOTAL_STOCK = db.Column(db.Integer) 
    CONDITION = db.Column(db.String(2000)) 
    LOCATION = db.Column(db.String(2000)) 
    TRANSFER_HISTORY = db.Column(db.String(2000)) 
    REMARKS = db.Column(db.String(2000)) 


@app.route('/')
def home():
    return render_template("login.html")
@app.route('/stock')
def stock():
    return render_template("stock.html")
@app.route('/stockadmin')
def stockadmin():
    return render_template("stockadmin.html")

@app.route('/addstock')
def addstock():
    return render_template("addstock.html")
@app.route('/nonconsumable')
def nonconsumable():
    return render_template("nonconsumable.html")

#admin credentials
admindata = {'stock@ucen': '123',
            'scholarship@ucen': '123',
            'bonafide@ucen':'123'}

#Admin authetication
@app.route('/admin_login', methods=['POST', 'GET'])
def login():
    name = request.form['adminusername']
    pwd = request.form['adminpassword']
    if name not in admindata:
        return render_template('login.html',
                               info='Invalid User !')
    elif admindata[name] != pwd:
         return render_template('login.html',
                                   info='Invalid Password !')
    elif name == 'stock@ucen':
        return render_template('stock.html')
    elif name == 'bonafide@ucen':
        return render_template('bonafide.html')
    elif name == 'scholarship@ucen':
        return render_template('scholarship.html')
    else:
        return render_template('login.html',
                               info='Invalid User !')

       
#faculty credentials
facultydata = {
    'it@ucen':'123',
    'ece@ucen':'123',
    'cse@ucen':'123',
    'civil@ucen':'123',
    'mech@ucen':'123',
    'eee@ucen':'123',
    'mba@ucen':'123'   
}
        
#faculty authentication
@app.route('/faculty_login', methods=['POST', 'GET'])
def faculty_login():
    name = request.form['facultyusername']
    pwd = request.form['facultypassword']
    if name not in facultydata:
        return render_template('login.html',
                               info='Invalid User !')
    
    elif facultydata[name] != pwd:
         return render_template('login.html',
                                   info='Invalid Password !')
                
    else: 
        if name in facultydata:
         return render_template('admin.html')
         
#student authentication & their profile view
@app.route('/student_login', methods=['POST', 'GET'])
def student_login():
    name = request.form['studentusername']
    pwd = request.form['studentpassword']
    student = student.query.filter_by(ROLL_NO=name, DOB_YYYY_MM_DD=pwd).first()
    
    if student:
      query = student.query.filter_by(ROLL_NO=name).first()      
      return render_template('studentprofileview.html',query=query)
    else:
       return render_template('login.html')
   

#faculty search for a student in nav bar
@app.route('/search', methods=['POST', 'GET'])
def search_student():
  reg = request.form['roll']
  search=student.query.filter_by(ROLL_NO=reg).first()
  return render_template('admin.html',search=search)

#edit student details by faculties
@app.route('/edit/<int:ROLL_NO>', methods=['GET', 'POST'])
def edit(ROLL_NO):
    post = student.query.filter_by(ROLL_NO=ROLL_NO).first()
    if request.method == 'POST':
        post.APPL_NO = request.form['appl_no']
        post.ROLL_NO = request.form['roll_no']
        post.NAME = request.form['name']
        db.session.commit()
        flash('student record updated successfully!', 'success')
    posts=student.query.filter_by(ROLL_NO=ROLL_NO).first()
    return render_template('edit.html', post=post,posts=posts)

#view all student details of their department
@app.route('/studentdetails')
def studentdetails():
    query=student.query.all() 
    return render_template('studentdetails.html',query=query)


#route to  updation page from faculty admin page
@app.route('/update')
def update():
    return render_template("update.html")
  
  
#update arrear
@app.route('/updatearrear', methods=['GET', 'POST'])
def updatearrear():
    regnum=request.form['regnum']
    post = student.query.filter_by(ROLL_NO=regnum).first()
    if request.method == 'POST':
        post.NO_OF_ARREARS = request.form['arrear']
        db.session.commit()
        flash('student record updated successfully!', 'success')
    return render_template('update.html', post=post)

#update placement
@app.route('/updateplacement', methods=['GET', 'POST'])
def updateplacement():
    regnum=request.form['regnum']
    post = student.query.filter_by(ROLL_NO=regnum).first()
    if request.method == 'POST':
        post.PLACEMENT_STATUS = request.form['placement']
        db.session.commit()
        flash('student record updated successfully!', 'success')
    return render_template('update.html', post=post)


#consumable stock view

@app.route('/consumable')
def consumable():
    query = stock_management.query.all()
    return render_template("consumable.html",query=query)


#add consumable product
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # retrieve form data from request object
        si_no = max(stock_management.SI_NO) +1
        stock_type = request.form['stock_type']
        department = request.form['department']
        product_id = request.form['product_id']
        date_of_purchase = request.form['date_of_purchase']
        bill_invoice_no = request.form['bill_invoice_no']
        bill_date = request.form['bill_date']
        equipment = request.form['equipment']
        no_of_quantity = int(request.form['no_of_quantity'])
        cost_per_unit = int(request.form['cost_per_unit'])
        total_cost = no_of_quantity * cost_per_unit
        supplier_name = request.form['supplier_name']
        warranty = request.form['warranty']
        warranty_period = request.form['warranty_period']
        total_stock = int(request.form['total_stock'])
        condition = request.form['condition']
        location = request.form['location']
        remarks = request.form['remarks']
        
        # create new consumable product object
        new_product = stock_management(SI_NO=si_no,STOCK_TYPE=stock_type,DEPARTMENT=department,PRODUCT_ID=product_id,DATE_OF_PURCHASE=date_of_purchase, BILL_INVOICE_NO=bill_invoice_no, BILL_DATE=bill_date,
                                          EQUIPMENT=equipment, NO_OF_QUANTITY=no_of_quantity, COST_PER_UNIT=cost_per_unit,
                                          TOTAL_COST=total_cost, SUPPLIER_NAME=supplier_name, WARRANTY=warranty, WARRANTY_PERIOD=warranty_period,
                                          TOTAL_STOCK=total_stock, CONDITION=condition, LOCATION=location, REMARKS=remarks)
        
        # add the new product to the database session and commit the changes
        db.session.add(new_product)
        db.session.commit()
        return render_template("addstock.html")
    
    
#bonafide generation
@app.route('/generate_bonafide', methods=['POST'])
def generate_bonafide():
    # Get the user's input from the HTML form
    rollno = request.form['rollno']
    post = student.query.filter_by(ROLL_NO=rollno).first()
    name = post.NAME
    refid = request.form['refid']
    date = datetime.date.today()
    formatted_date = date.strftime("%d-%m-%Y")
    gender = post.GENDER
    if gender == 'MALE':
        salutation = 'Mr.'
        pronoun = 'He'
    else:
        salutation = 'Mrs.'
        pronoun = 'She'

    father_name = post.FATHER_NAME
    mother_name = post.MOTHER_NAME
    year = post.YEAR
    degree = post.DEGREE
    department = post.BRANCH
    current_year = datetime.datetime.now().year
    next_year = current_year + 1

    # Create a new PDF document
    filename = f"{name}_bonafide.pdf"
    document = canvas.Canvas(filename, pagesize=A4)

    # Set the font and font size
    document.setFont("Times-Bold", 14)
    
    logo_path = 'static/aulogo.png'
    logo = ImageReader(logo_path)
    document.drawImage(logo, 30, 780, width=50, height=50)

    # Add the content
    document.drawString(130, 810, "UNIVERSITY COLLEGE OF ENGINEERING, NAGERCOIL")
    document.drawString(160, 790, "(A Constituent College Of Anna University, Chennai)")
    document.drawString(0, 770, "______________________________________________________________________________________________________")
    document.drawString(30, 755, "Dr. V.A. Nagarajan")
    document.drawString(30, 740, "DEAN")
    document.drawString(410, 755, "Phone: 04652-260510")
    document.drawString(410, 740, "E-Mail: deanucen@gmail.com")
    document.drawString(0, 735, "______________________________________________________________________________________________________")
    document.drawString(30, 715, f"Ref : {refid}")
    document.drawString(430, 715, f"Date : {formatted_date}")
    document.drawString(230, 660, "BONAFIDE CERTIFICATE")
    document.setFont("Times-Roman", 14)
    document.drawString(80, 630, f"This is to certify that {salutation} {name}, (Reg. No: {rollno})")
    document.drawString(30, 610, f"S/o. Mr. {father_name} & Mrs. {mother_name} is a bonafide student of")
    document.drawString(30, 590, f"University College of Engineering, Nagercoil. {pronoun} Studies {year} Year {degree} in the Department of ")
    document.drawString(30, 570, f"{department} during the academic year {current_year} - {next_year} ")
    
    # Save the PDF document
    document.showPage()
    document.save()

    # Serve the PDF document as a response to the user
    response = make_response(open(filename, 'rb').read())
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set('Content-Disposition', 'attachment', filename=filename)
    return response


if __name__ == '__main__':
    app.run(debug=True)
