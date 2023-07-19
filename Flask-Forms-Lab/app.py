from flask import Flask, jsonify, request, render_template, redirect, url_for
import random


app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

name_in = ""
username = "siwarha"
password = "123"
facebook_friends = ["Loai","Kenda","Avigail", "George", "Fouad", "Gi", "Gabby", "Shiraz", "Ilay"]


@app.route('/', methods = ['GET', 'POST'])
def login():
  if request.method == 'GET': #check if this is a GET request
        return render_template('login.html')
  else:
  	    if request.form['username'] == username and request.form['password'] == password:
  	    	return redirect(url_for('home',username = username, password = password))
  	    else:
  	    	print("wrong user name or password")
  	    	return render_template('login.html')

@app.route('/home')
def home():
	 return render_template('home.html', friends = facebook_friends)


@app.route('/friend_exists/<string:name>')
def hello_name_route(name):
	  if name in facebook_friends:
	  	
	  	return render_template('friend_exists.html', n = name, friends = facebook_friends, name_in = True)
	  else:
	  	
	  	return render_template('friend_exists.html', n = name, friends = facebook_friends, name_in = False)






if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
