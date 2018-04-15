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
@app.route('/', methods=['GET', 'POST'])
def main():
	# Select collection based on coin requested
	coin = request.args.get('coin')
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
	# Get scope for Polarity Aggregate Query
	scope = request.args.get('scope')
	if scope == 'month':
		# Pipeline for Polarity Aggreagate Query MONTH
		pipeline = [
			{ "$group": {
				"_id": {
					"month" : {
						"$month": "$timestamp"
					}
				},
				"avgPolarity" : { "$avg" : "$polarity" },
				"count": { "$sum": 1 }
			}},
			{ "$sort": { "_id": 1 }}
		]
	elif scope == 'week':
		# Pipeline for Polarity Aggreagate Query WEEK
		pipeline = [
			{ "$group": {
				"_id": {
					"week" : {
						"$week": "$timestamp"
					}
				},
				"avgPolarity" : { "$avg" : "$polarity" },
				"count": { "$sum": 1 }
			}},
			{ "$sort": { "_id": 1 }}
		]
	else:
		scope = 'day'
		# Pipeline for Polarity Aggreagate Query DAY
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
	return render_template('index.html', coin=coin, scope=scope, polarities=polarities)
