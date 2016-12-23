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
            tour = getTour(hit['_source']['tourId'])
            tour['historyid'] = hit['_id']
            tour['takenOn'] = hit['_source']['takenOn']
            result_list.append(tour)
    return result_list

def getTour(tourid):
    result_list = []
    body = {"query": {"match_phrase": {"_id":tourid}}}
    result = mapping.elasticSearch('tour-index',body)
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            _id = hit['_id']
            name = hit['_source']['name']
            createdBy = hit['_source']['createdBy']
            category = hit['_source']['category']
            time = hit['_source']['time']
            distance = hit['_source']['distance']
            stops = hit['_source']['stops']
            latitude = hit['_source']['latitude']
            longitude = hit['_source']['longitude']
            return (dict(tourid=_id,name=name, createdBy=createdBy, category=category, time=time,distance=distance,stops=stops,latitude=latitude,longitude=longitude))
