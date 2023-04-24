from datetime import datetime
import hashlib
from flask import(
    Flask,
    request,
    render_template,
    redirect,
    session,
    url_for,
)
from dal import UserAccount
from model import user
app=Flask(__name__)
app.secret_key='1234'

@app.route('/')
def index():
    return render_template('login.html') 

@app.route('/signupView')
def signupView():
    return render_template('signup.html')

@app.route('/loginView')
def loginView():
    return render_template('login.html')

@app.route('/loginView', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form['email']
        pwd = request.form['password']
        user_account = UserAccount()  # Create an instance of UserAccount
        if user_account.Login(user(name, pwd)):
            response = app.make_response(render_template('app.html'))
            session['user_id'] = name
            return response
        else:
            return render_template('signup.html', error_auth='login or password incorrect')
    else:
        if 'user_id' in session:
            return render_template('app.html')
        return redirect('/') 
    
@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return redirect('/')


if(__name__ == "__main__"):
    app.run(host="0.0.0.0",port=9090, debug=True)