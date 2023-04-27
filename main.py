from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import login_required,current_user
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ucenofficeautomation'

#database Configuration
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/studentprofile'
db=SQLAlchemy(app)

#Table for studnt details
class year(db.Model):
    SL_NO = db.Column(db.Integer, primary_key=True)
    APPL_NO = db.Column(db.String(50))
    ROLL_NO = db.Column(db.Integer)
    NAME = db.Column(db.String(50)) 
    DOB_YYYY_MM_DD  = db.Column(db.String(50))  
    GENDER = db.Column(db.String(50))
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
    NO_OF_ARREAR = db.Column(db.Integer) 
    PLACEMENT_STATUS = db.Column(db.String(100))


@app.route('/')
def home():
    return render_template("login.html")
@app.route('/stock')
def stock():
    return render_template("stock.html")
@app.route('/stockadmin')
def stockadmin():
    return render_template("stockadmin.html")
@app.route('/consumable')
def consumable():
    return render_template("consumable.html")
@app.route('/addstock')
def addstock():
    return render_template("addstock.html")
@app.route('/nonconsumable')
def nonconsumable():
    return render_template("nonconsumable.html")

#admin credentials
admindata = {'stock@ucen': '123',
            'scholarship@ucen': '123', }

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
            
    elif admindata[name] == admindata['stock@ucen']:
        
            return render_template('stock.html')
         
    else:
       if admindata[name] == admindata['scholarship@ucen']:
           
           return render_template('scholarship.html')
       
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
    student = year.query.filter_by(ROLL_NO=name, DOB_YYYY_MM_DD=pwd).first()
    
    if student:
      query = year.query.filter_by(ROLL_NO=name).first()      
      return render_template('studentprofileview.html',query=query)
    else:
       return render_template('login.html')
   

#faculty search for a student in nav bar
@app.route('/search', methods=['POST', 'GET'])
def search_student():
  reg = request.form['roll']
  search=year.query.filter_by(ROLL_NO=reg).first()
  return render_template('admin.html',search=search)

#edit student details by faculties
@app.route('/edit/<int:ROLL_NO>', methods=['GET', 'POST'])
def edit(ROLL_NO):
    post = year.query.filter_by(ROLL_NO=ROLL_NO).first()
    if request.method == 'POST':
        post.APPL_NO = request.form['appl_no']
        post.ROLL_NO = request.form['roll_no']
        post.NAME = request.form['name']
        db.session.commit()
        flash('Year record updated successfully!', 'success')
    posts=year.query.filter_by(ROLL_NO=ROLL_NO).first()
    return render_template('edit.html', post=post,posts=posts)

#view all student details of their department
@app.route('/studentdetails')
def studentdetails():
    # query=db.engine.execute(f"SELECT * FROM `student`") 
    query=year.query.all() 
    return render_template('studentdetails.html',query=query)


#route to  updation page from faculty admin page
@app.route('/update')
def update():
    return render_template("update.html")
  
  
#update arrear
@app.route('/arrearupdation', methods=['GET', 'POST'])
def arrearupdation():
    if request.method == 'POST':
        year.NO_OF_ARREAR = request.form['arrear']
        db.session.commit()
        flash('Year record updated successfully!', 'success')
    return render_template('update.html', year=year)

if __name__ == '__main__':
    app.run(debug=True)
