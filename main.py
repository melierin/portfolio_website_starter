from flask import Flask, render_template, request, redirect, url_for, app
import os



app = Flask(__name__)
IS_DEV = app.debug == 'development'


@app.route("/")
def home():
	return render_template("index.html")




if __name__ == '__main__':
	os.environ['FLASK_DEBUG'] = 'development'
	app.run(debug=True)
	
	