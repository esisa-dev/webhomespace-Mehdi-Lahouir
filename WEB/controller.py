from datetime import datetime
import hashlib
import os
from flask import(
    Flask,
    jsonify,
    request,
    render_template,
    redirect,
    send_file,
    session,
    url_for,
)
from dal import UserAccount
from model import user
app=Flask(__name__)
app.secret_key='1234'
size=0
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
        user_account = UserAccount()  
        if user_account.Login(user(name, pwd)):
            response = app.make_response(render_template('app.html'))
            session['user_id'] = name
            session['password']= pwd
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
    session.pop('password',None)
    return redirect('/')

@app.route('/download')
def Download():
    if session['user_id'] is None or session['password'] is None: 
        return redirect('/')
    else:
        user_account = UserAccount()  
        user_account.zipfile(user(session['user_id'],session['password']))
        return send_file('/tmp/homedir.zip', as_attachment=True)
    
@app.route('/files')
def get_files():
    files = []
    size=0
    path = os.path.expanduser("/home/rike")
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)) or os.path.isdir(os.path.join(path, filename)):
            stats = os.stat(os.path.join(path, filename))
            modified = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            if os.path.isfile(os.path.join(path, filename)):
                filetype = 'File'
            else:
                filetype = 'Directory'
            files.append({'name': filename, 'type': filetype, 'size': stats.st_size, 'modified': modified})
    return jsonify(files),size

def count_directories(path):
    count = 0
    for dirpath, dirnames, filenames in os.walk(path):
        count += len(dirnames)
    return count

if(__name__ == "__main__"):
    app.run(host="0.0.0.0",port=8800, debug=True)