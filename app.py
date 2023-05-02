""" Web app for the project"""

from flask import Flask, session, render_template, request, redirect, Response
import pyrebase

app = Flask(__name__)

config = {
    'apiKey': "AIzaSyC_5M7TaDgNf6J2AXxdJncGR5oOiVUPdDY",
    'authDomain': "authentication-8898c.firebaseapp.com",
    'projectId': "authentication-8898c",
    'storageBucket': "authentication-8898c.appspot.com",
    'messagingSenderId': "980677145913",
    'appId': "1:980677145913:web:53e3ddeffac9e4617da4e8",
    'measurementId': "G-QZ3FM7J3D7",
    'databaseURL': ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = "secret key"


@app.route('/', methods=['POST', 'GET'])
def index() -> str:
    """Renders the index page"""
    if 'user' in session:
        return 'Hi, {}'.format(session['user'])
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
        except:
            return 'Failed to login'
    return render_template('home.html')


@app.route('/logout')
def logout() -> Response:
    """Logs out the user"""
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(port=1111)
