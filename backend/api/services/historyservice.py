from api import mapping

def fullhistory():
    result_list = []
    result = mapping.elasticSearch('history-index')
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            awsid = hit['_id']
            id = hit['_source']['id']
            userid = hit['_source']['userId']
            tourid = hit['_source']['tourId']
            takenon = hit['_source']['takenOn']
            result_list.append(dict(awsid=awsid,id=id, userid=userid, tourid=tourid, takenon=takenon))
    return result_list

def userhistory(userid):
    result = []
    # query to search based on userid

    #result_list.append(dict(awsid=awsid,id=id, userid=userid, tourid=tourid, takenon=takenon))

    return result
