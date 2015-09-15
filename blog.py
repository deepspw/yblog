from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)

# from sqlalchemy import create_engine, asc, desc, func, update
# from sqlalchemy.orm import sessionmaker

@app.route('/')
def homepage():
	title = "Waiyin Lau - Rigger/Character TD"
	paragraph = ["Line 1", "Line 2"]
	return render_template("index.html", title = title , paragraph = paragraph)



if __name__ == "__main__":
	app.run(debug=True)