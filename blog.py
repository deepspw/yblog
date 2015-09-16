from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)

# from sqlalchemy import create_engine, asc, desc, func, update
# from sqlalchemy.orm import sessionmaker

@app.route('/')
def homepage():
	title = "Waiyin Lau - Rigger/Character TD"
	posttitle = "Insert Post Title Here"
	postcontent = "paragraph of content here"
	return render_template("index.html", title = title , posttitle = posttitle, postcontent = postcontent)

@app.route('/reel/')
def reel():
	return render_template('index.html')

@app.route('/scripts/')
def scripts():
	return render_template('index.html')

@app.route('/about/')
def about():
	return render_template('index.html')

@app.route('/cv/')
def cv():
	return render_template('index.html')

@app.route('/contact/')
def contact():
	return render_template('index.html')

@app.route('/blog/')
def blog():
	return render_template('index.html')

@app.route('/doodles/')
def doodles():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)