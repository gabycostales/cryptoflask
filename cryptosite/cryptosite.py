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
	# Select collection based on coin requested
	if coin == 'ETH':
		collection = db.ETH
	elif coin == 'LTC':
		collection = db.LTC
	elif coin == 'SUMO':
		collection = db.SUMO
	elif coin == 'TRX':
		collection = db.TRX
	else:
		coin = 'BTC'
		collection = db.BTC
	# Pipeline for Aggreagate Query
	pipeline = [
		{ "$group": {
			"_id": {
				"day" : {
					"$dateToString": {
						"format": "%Y-%m-%d",
						"date": "$timestamp"
					}
				}
			},
			"avgPolarity" : { "$avg" : "$polarity" },
			"count": { "$sum": 1 }
		}},
		{ "$sort": { "_id": 1 }},
		{ "$limit": 7 }
	]
	# Query for average polarities by day
	cursor = collection.aggregate(pipeline)
	# Build array of polarites to pass
	polarities = []
	for doc in cursor:
		polarities.append(doc['avgPolarity'])
	print(polarities)
	# Render page
	return render_template('index.html', coin=coin, polarities=polarities)
