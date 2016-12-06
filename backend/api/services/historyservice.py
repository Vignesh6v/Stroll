from api import mapping

def fullhistory():
    result_list = []
    result = mapping.elasticSearch('history-index')
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            _id = hit['_id']
            userid = hit['_source']['userId']
            tourid = hit['_source']['tourId']
            takenon = hit['_source']['takenOn']
            result_list.append(dict(historyid=_id, userid=userid, tourid=tourid, takenon=takenon))
    return result_list

def userhistory(userid):
    result_list = []
    body = {"query": {"match_phrase": {"userId":userid}}}
    result = mapping.elasticSearch('history-index',body)
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            _id = hit['_id']
            takenOn = hit['_source']['takenOn']
            tourId = hit['_source']['tourId']
            result_list.append(dict(historyid=_id,tourId=tourId, takenOn=takenOn))
    return result_list
