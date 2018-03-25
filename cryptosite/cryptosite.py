from flask import Flask, request, render_template, redirect
from pymongo import MongoClient

# configuration
DEBUG = True
client = MongoClient('localhost:27017')
db = client.cryptoDB

# create the app
app = Flask('cryptosite')
app.config.from_object(__name__)
app.config.from_envvar('CRYPTOSITE_SETTINGS', silent=True)

# Main/Index Route
@app.route('/')
@app.route('/<coin>')
def main(coin='BTC'):
	return render_template('index.html', coin=coin)
