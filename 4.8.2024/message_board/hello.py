from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

all_visitors = []

@app.route('/hello')
def hello():
	name = request.args.get('name')
	all_visitors.append(name)
	print(all_visitors)
	return render_template('hello.html', name=name)