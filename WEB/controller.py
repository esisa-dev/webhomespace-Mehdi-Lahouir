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
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html') 

@app.route('/signupView')
def signupView():
    return render_template('signup.html')

@app.route('/loginView')
def loginView():
    return render_template('login.html')

if(__name__ == "__main__"):
    app.run(host="0.0.0.0",port=9090, debug=True)