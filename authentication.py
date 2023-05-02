""" Simple authentication webpage login"""

import pyrebase

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

email = 'test@gmail.com'
password = 'test123'

# user = auth.create_user_with_email_and_password(email, password)
# print(user)

user = auth.sign_in_with_email_and_password(email, password)
# info = auth.get_account_info(user['idToken'])
# print(info)

# auth.send_email_verification(user['idToken'])
auth.send_password_reset_email(email)
