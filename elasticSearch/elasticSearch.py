import json
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import datetime

user={}
tour={}
stops={}
history={}
photo={}

def createUserIndex():
	user["id"] = "0000001" 
	user["email"]= "rdk.ashwin@yahoo.com"
	user["firstName"]= "Radhakrishnan"
	user["lastName"]= "Moni"
	user["password"]= "password123"
	final = json.dumps(user)
	res = es.index(index="user-index", doc_type='user', id=user["id"], body=final)
	print(res['created'])

def createTourIndex():
	tour["id"] = "t0000001"
	tour["name"] = "coffee"
	tour["createdBy"] = "Radhakrishnan"
	tour["category"] = "food"
	tour["time"] = "40"
	tour["distance"] = "8"
	tour["stops"] = "4"
	final = json.dumps(tour)
	res = es.index(index="tour-index", doc_type='tour', id=tour["id"], body=final)
	print(res['created'])

def createStopsIndex():
	location = {'latitude' : '23.34566', 'longitude' : '56.234234'}
	stops["id"] = "s0000001"
	stops["tourId"] = "t0000001"
	stops["sequence"] = "2"
	stops["stopName"] = "au bon pain"
	stops["location"] = location
	stops["photoId"] = "p0000001"
	stops["descriptionId"] = "d0000001"
	final = json.dumps(stops)
	res = es.index(index="stops-index", doc_type='stops', id=stops["id"], body=final)
	print(res['created'])


def createHistoryIndex():
	history["id"] = "h0000001"
	history["userId"] = "0000001"
	history["tourId"] = "t0000001"
	history["takenOn"] = str(datetime.datetime.now())
	final = json.dumps(history)
	res = es.index(index="history-index", doc_type='history', id=history["id"], body=final)
	print(res['created'])

def createPhotoIndex():
	photo["id"] = "0000001"
	photo["userId"] = "0000001"
	photo["name"] = "aubonpain.jpg"
	photo["photoId"] = "p0000001"
	final = json.dumps(photo)
	res = es.index(index="photo-index", doc_type='photo', id=photo["id"], body=final)
	print(res['created'])



if __name__ == '__main__':
	host = ''
	awsauth = AWS4Auth('', '', 'us-east-1', 'es')

	es = Elasticsearch(
			hosts=[{'host': host, 'port': 443}],
			http_auth=awsauth,
			use_ssl=True,
			verify_certs=True,
			connection_class=RequestsHttpConnection
	)
	#createUserIndex();
	#createTourIndex();
	#createStopsIndex();
	createHistoryIndex();
	createPhotoIndex();