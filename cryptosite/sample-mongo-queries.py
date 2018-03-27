from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.cryptoDB

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
	{ "$sort": { "_id": 1 }}
	  
]

print("AVERAGE POLARITY ALL TIME")
print("=========================")

print("Sentiments for BTC")
btcCursor = db.BTC.aggregate(pipeline)
for doc in btcCursor:
	print(doc)

print("Sentiments for ETH")
ethCursor = db.ETH.aggregate(pipeline)
for doc in ethCursor:
	print(doc)

print("Sentiments for LTC")
ltcCursor = db.LTC.aggregate(pipeline)
for doc in ltcCursor:
	print(doc)

print("Sentiments for SUMO")
sumoCursor = db.SUMO.aggregate(pipeline)
for doc in sumoCursor:
	print(doc)

print("Sentiments for TRX")
trxCursor = db.TRX.aggregate(pipeline)
for doc in trxCursor:
	print(doc)
