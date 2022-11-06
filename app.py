from flask import *
from flask_mysqldb import *


app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tiger'
app.config['MYSQL_DB'] = 'customer'
 
mysql = MySQL(app)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login')
def login():
    if request.method == 'POST':
        print("login details")
    return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        userdetail=request.form
        cur=mysql.connection.cursor()
        firstname=userdetail['firstname']
        lastname=userdetail['lastname']
        email=userdetail['email']
        mnumber=userdetail['number']
        password=userdetail['password']
        password2=userdetail['password2']
        cur.execute("INSERT INTO customerdetails(firstname,lastname,email,mobilenumber,password) values(%s, %s, %s, %s , %s)",(firstname,lastname,email,mnumber,password))
        mysql.connection.commit()
        cur.close()
        return render_template('success.html')
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)

