from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hello')
def hello():
	name = request.args.get('name')

	return f'<h1>Hello {name}!</h1><p>It is almost time to go home</p>'