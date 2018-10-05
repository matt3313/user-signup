from flask import Flask, request, redirect, render_template
import cgi
import os
import re



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/sign-up")
def index():
    
    return render_template('index.html')


def is_empty(field):
    if len(field) < 1:
        return True
    else:
        return False

def is_space(field):
    if ' ' in field:
        return True
    else:
        return False


@app.route("/sign-up", methods=['POST'])
def validate_form():

    user_name = request.form['username']
    password = request.form['password']
    verify_password = request.form['password1']
    error_user_name = ''
    password_error = ''
    password_error1 = ''
    error_email = ''
    email = request.form['email']
    invalid_username = 'Thats not a valid user name'
    invalid_password = 'Thats not a valid password'
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if is_empty(user_name):
        error_user_name = invalid_username

    if is_space(user_name):
        error_user_name = invalid_username

    elif len(user_name) < 3:
        error_user_name = invalid_username
        
    if email != '' and match == None:
        error_email = 'Invalid email'

    if is_space(password):
        password_error = invalid_password

    if is_space(verify_password):
        password_error1 = invalid_password

    if len(password) < 3:
        password_error = invalid_password
        password = ''
        verify_password = ''
    elif password != verify_password:
        password_error = 'Passwords do not match'
        password_error1 = 'Passwords do not match'
        password = ''
        verify_password = ''


    if not error_user_name and not error_email and not password_error and not password_error1:
        return redirect("/welcome?username={0}".format(user_name))

    else:
        return render_template('index.html', error_user_name=error_user_name, user_name=user_name, \
        email=email, error_email=error_email, password_error = password_error, password_error1 = password_error1)

@app.route("/welcome")
def wecolme():
    user_name = request.args.get('username')
    return render_template("welcome.html", username = user_name)
           


app.run()