from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('credentials.txt')

access_token = config.get("AWS","access_token")
access_token_secret = config.get("AWS","access_token_secret")
region = config.get("AWS","region")
host = config.get("AWS","host")

awsauth = AWS4Auth(access_token, access_token_secret, region, 'es')
es = Elasticsearch(
	hosts=[{'host': host, 'port': 443}],
	http_auth=awsauth,
	use_ssl=True,
	verify_certs=True,
	connection_class=RequestsHttpConnection
)

def elasticSearch(index,body={}):
    result = es.search(index=index, body=body)
    return result

def elasticInsert(index,doc_type,body):
    result = es.index(index=index,doc_type=doc_type, body=body)
    return result
