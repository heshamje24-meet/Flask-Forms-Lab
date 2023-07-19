from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
user={'hesham': '123',
    'razi': '321'}


facebook_friends=["ahmad","ameer","hasan", "adam", "yazan", "razi"]


@app.route('/')  # '/' for the default page
def index():
  return render_template('login.html')
@app.route('/home',methods=['POST','GET'])
def login():
     if request.method=='POST':
          username = request.form['username']
          password = request.form['password']
          if username in user and user[username] == password:
               return render_template('home.html',friends=facebook_friends)
          else:
            return render_template('login.html',message='Invalid credentials. Please try again')
     else:
     	return redirect(url_for('home.html'))
          
@app.route('/friends_exist/<string:name>',methods=['GET','POST'])
def friend_exists(name):
    exists = name
    return render_template('friend_exists.html', name=name, friends=facebook_friends)

        

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)